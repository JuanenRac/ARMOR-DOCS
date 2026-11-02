#!/usr/bin/env bash
# ARMOR-DOCS - install the pre-commit hook of publication_check in one repository (or in every ARMOR-* repository next to this one).
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
#
#   tools/install_hooks.sh ARMOR-SERVER      # one repository
#   tools/install_hooks.sh --all             # every ARMOR-* repository next to this one
#
# The hook refuses a commit that stages a private key, a secrets file, a public address, a personal e-mail or a build setting that carries a secret. It reads what is staged, not the history,
# and it never prints a secret. A hook that was there already is kept as pre-commit.before and run first.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FAMILY="$(cd "$HERE/../.." && pwd)"
targets=()
if [[ "${1:-}" == "--all" ]]; then
  for repo in "$FAMILY"/ARMOR-*; do [[ -d "$repo/.git" ]] && targets+=("$repo"); done
elif [[ -n "${1:-}" ]]; then
  targets+=("$FAMILY/$1")
else
  echo "usage: tools/install_hooks.sh <ARMOR-REPOSITORY>|--all" >&2; exit 2
fi
for repo in "${targets[@]}"; do
  [[ -d "$repo/.git" ]] || { echo "SKIP $(basename "$repo"): not a git repository"; continue; }
  hook="$repo/.git/hooks/pre-commit"
  if [[ -f "$hook" ]] && ! grep -q "armor-publication-check" "$hook"; then mv "$hook" "$hook.before"; fi
  cat >"$hook" <<'HOOK'
#!/usr/bin/env bash
# armor-publication-check (installed by ARMOR-DOCS/tools/install_hooks.sh)
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[[ -x "$here/pre-commit.before" ]] && { "$here/pre-commit.before" || exit $?; }
repo="$(cd "$here/../.." && pwd)"
checker="$(dirname "$repo")/ARMOR-DOCS/tools/publication_check.py"
[[ -f "$checker" ]] || exit 0
python3 "$checker" --staged "$(basename "$repo")" 2>/dev/null || python "$checker" --staged "$(basename "$repo")"
HOOK
  chmod +x "$hook"
  echo "OK   $(basename "$repo"): pre-commit installed"
done
