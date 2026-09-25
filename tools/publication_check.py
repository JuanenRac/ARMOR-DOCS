#!/usr/bin/env python3
"""ARMOR-DOCS - what would leak if the repositories were published.

Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.

    python tools/publication_check.py            # every ARMOR-* repository next to this one, tracked files and history
    python tools/publication_check.py ARMOR-RADAR --no-history

It reads git only (tracked files, and with history every revision, commit authors and messages), never the ignored files, and it never
prints the matched secret: a finding shows the file, the line number and the kind, with the value cut to its first characters.

BLOCK  something that must not go public: a private key, a public IP address, a personal e-mail address, a tracked secrets/ or .env
       file, a commit with a co-author or AI trailer, a commit author other than the project's.
REVIEW a line that looks like a literal password or token and needs a human look (test fixtures and documentation examples are common).

The exit status is 1 when anything is BLOCK, so a publication pipeline can refuse. Nothing here proves the absence of a secret.
"""
from __future__ import annotations

import ipaddress
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALLOWED_AUTHOR = "Electro Hobby 3D <electrohobby3d@gmail.com>"
PUBLIC_EMAILS = {"electrohobby3d@gmail.com"}   # the project's own public address

PRIVATE_KEY = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@(?:gmail|hotmail|outlook|yahoo|icloud|proton(?:mail)?)\.[a-z]{2,}\b", re.I)
IPV4 = re.compile(r"(?<![\d.])(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?![\d.])")
LITERAL = re.compile(r"""(?ix)\b(pass(?:word|wd)?|secret|token|api[_-]?key|psk)\b["']?\s*[:=]\s*["']([^"'\s$`{}<>()]{8,})["']""")
BAD_PATH = re.compile(r"(^|/)(secrets/(?!.*example)|\.env$|.*\.env$|.*\.pem$|.*\.key$|id_[a-z0-9]+$)", re.I)
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".webp", ".pdf", ".zip", ".gz", ".bin", ".woff", ".woff2", ".ttf", ".jar", ".apk", ".stl", ".step", ".fcstd"}
# addresses that are public but say nothing about anyone: the well-known DNS resolvers and the boundary values that the private-address tests use
BENIGN_IPS = {"8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1", "9.9.9.9", "1.2.3.4", "8.8.8.0", "8.0.0.1", "11.0.0.1", "172.15.0.1", "172.32.0.1", "192.169.0.1", "172.15.255.255", "172.32.0.0"}
# words that make a "literal" obviously not a secret
HARMLESS = re.compile(r"(?i)(example|placeholder|changeme|change-me|your[-_ ]|xxxx|\*{4}|test|fake|dummy|sample|correct-horse|adminpass|secret-for|0000|1111|aaaa|cccc|iiii|kkkk|oooo|\.\.\.)")


def git(repo: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed in {repo.name}: {result.stderr.strip()[:200]}")
    return result.stdout


def public_ip(text: str) -> bool:
    try:
        address = ipaddress.ip_address(text)
    except ValueError:
        return False
    return address.is_global and not address.is_multicast and not text.startswith(("0.", "255."))


def scan_text(name: str, where: str, text: str, findings: list[tuple[str, str, str, str]]) -> None:
    for number, line in enumerate(text.splitlines(), 1):
        if len(line) > 2000:
            continue
        ref = f"{where}:{number}"
        if PRIVATE_KEY.search(line):
            findings.append(("BLOCK", name, ref, "private key"))
        for match in EMAIL.finditer(line):
            if match.group(0).lower() in PUBLIC_EMAILS:
                continue
            findings.append(("BLOCK", name, ref, f"personal e-mail {match.group(0)[:4]}..."))
        for match in IPV4.finditer(line):
            candidate = match.group(1)
            if all(0 <= int(part) <= 255 for part in candidate.split(".")) and candidate not in BENIGN_IPS and public_ip(candidate) and not re.search(r"(?i)version|v\d+\.\d+\.\d+\.\d+|\d+\.\d+\.\d+\.\d+-", line[max(0, match.start() - 12):match.end() + 1]):
                findings.append(("BLOCK", name, ref, f"public IP address {candidate.split('.')[0]}.x.x.x"))
        for match in LITERAL.finditer(line):
            value = match.group(2)
            if not HARMLESS.search(value) and not HARMLESS.search(line) and len(set(value)) > 3:
                findings.append(("REVIEW", name, ref, f"literal {match.group(1).lower()} {value[:3]}..."))


def check_repo(repo: Path, history: bool) -> list[tuple[str, str, str, str]]:
    name = repo.name
    findings: list[tuple[str, str, str, str]] = []
    tracked = [path for path in git(repo, "ls-files").splitlines() if path]
    for path in tracked:
        if BAD_PATH.search(path):
            findings.append(("BLOCK", name, path, "a secrets, key or environment file is tracked"))
        if Path(path).suffix.lower() in BINARY_SUFFIXES:
            continue
        try:
            text = (repo / path).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        scan_text(name, path, text, findings)
    log = git(repo, "log", "--all", "--format=%H%x1f%an <%ae>%x1f%cn <%ce>%x1f%B%x1e")
    for record in [r for r in log.split("\x1e") if r.strip()]:
        parts = record.strip("\n").split("\x1f", 3)
        if len(parts) < 4:
            continue
        sha, author, committer, message = parts[0][:10], parts[1], parts[2], parts[3]
        if author != ALLOWED_AUTHOR or committer != ALLOWED_AUTHOR:
            findings.append(("BLOCK", name, f"commit {sha}", f"author or committer is not the project's ({author.split('<')[0].strip()})"))
        if re.search(r"(?im)^(co-authored-by|generated with|signed-off-by)\b", message) or "claude" in message.lower():
            findings.append(("BLOCK", name, f"commit {sha}", "the message has a co-author, AI or sign-off trailer"))
    if history:
        seen: set[tuple[str, str]] = set()
        revisions = git(repo, "rev-list", "--all").split()
        for revision in revisions:
            names = git(repo, "ls-tree", "-r", "--name-only", revision).splitlines()
            for path in names:
                if BAD_PATH.search(path) and ("path", path) not in seen:
                    seen.add(("path", path))
                    findings.append(("BLOCK", name, f"{path} @ {revision[:10]}", "a secrets, key or environment file was tracked in the history"))
        # removed lines only: what was once committed and later taken out is still public
        diff = git(repo, "log", "--all", "-p", "--no-color", "--diff-filter=MD", "--unified=0", "--format=commit %h", check=False)
        current = ""
        for number, line in enumerate(diff.splitlines(), 1):
            if line.startswith("commit "):
                current = line[7:]
            elif line.startswith("-") and not line.startswith("---"):
                extra: list[tuple[str, str, str, str]] = []
                scan_text(name, f"history {current}", line[1:], extra)
                for item in extra:
                    key = (item[2], item[3])
                    if key not in seen:
                        seen.add(key)
                        findings.append((item[0], item[1], item[2].rsplit(":", 1)[0] + " (a removed line)", item[3]))
    return findings


def main(argv: list[str]) -> int:
    history = "--no-history" not in argv
    names = [a for a in argv if not a.startswith("--")]
    repos = [ROOT / n for n in names] if names else sorted(p for p in ROOT.glob("ARMOR-*") if (p / ".git").exists())
    blocked = 0
    for repo in repos:
        findings = check_repo(repo, history)
        block = [f for f in findings if f[0] == "BLOCK"]
        review = [f for f in findings if f[0] == "REVIEW"]
        blocked += len(block)
        print(f"{repo.name:24} BLOCK {len(block):3}  REVIEW {len(review):3}")
        for kind, _name, ref, what in findings[:60]:
            print(f"   {kind:6} {ref}  {what}")
        if len(findings) > 60:
            print(f"   ... and {len(findings) - 60} more")
    print("PUBLICATION_CHECK=" + ("FAIL" if blocked else "PASS"))
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
