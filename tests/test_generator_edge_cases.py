"""Edge cases of the generators (README, catalogue, publication check): language tables, anchors, figure words and the limits of the secret scan."""
import json
import re
import unittest
from unittest import mock

import _support  # noqa: F401  (puts tools/ on the path)

import make_catalog
import make_readmes as readmes
import publication_check as check

CODES = ["en", "es", "fr", "it", "de", "zh", "ja", "pt"]


class LanguageTableTests(unittest.TestCase):
    def test_eight_languages_in_the_documented_order(self):
        self.assertEqual([code for code, *_ in readmes.LANGUAGES], CODES)

    def test_file_names_are_unique_and_follow_the_readme_pattern(self):
        names = [file for _, file, *_ in readmes.LANGUAGES]
        self.assertEqual(len(set(names)), 8)
        self.assertEqual(names[0], "README.md")
        for name in names[1:]:
            self.assertRegex(name, r"^README_[a-z]{3}\.md$")

    def test_flags_and_names_are_unique_and_not_empty(self):
        for index in (2, 3):
            values = [row[index] for row in readmes.LANGUAGES]
            self.assertEqual(len(set(values)), 8)
            self.assertTrue(all(values))

    def test_every_language_has_ui_and_screenshot_heading(self):
        self.assertEqual(sorted(readmes.UI), sorted(CODES))
        self.assertEqual(sorted(readmes.SHOTS_HEADING), sorted(CODES))

    def test_every_language_translates_every_section_word(self):
        keys = [key for key in readmes.UI["en"] if key.startswith("s_")]
        for code in CODES:
            for key in keys:
                self.assertTrue(readmes.UI[code].get(key, "").strip(), f"{code} lacks {key}")

    def test_portuguese_is_european(self):
        text = " ".join(str(value) for value in readmes.UI["pt"].values())
        for brazilian in ("arquivo", "celular", "tela "):
            self.assertNotIn(brazilian, text.lower(), brazilian)

    def test_section_title_for_each_language_starts_with_the_icon(self):
        for code in CODES:
            for section, icon in readmes.SECTIONS:
                if section in ("screenshots",):
                    continue
                if not readmes.UI[code].get("s_" + section):
                    continue
                self.assertTrue(readmes.section_title(code, section).startswith(icon + " "))

    def test_screenshots_title_uses_its_own_heading(self):
        for code in CODES:
            self.assertIn(readmes.SHOTS_HEADING[code], readmes.section_title(code, "screenshots"))

    def test_jump_and_body_sections_are_known_sections(self):
        known = {name for name, _ in readmes.SECTIONS}
        self.assertTrue(set(readmes.BODY_SECTIONS) <= known)
        self.assertTrue(set(readmes.JUMP_SECTIONS) <= known)


class AnchorTests(unittest.TestCase):
    def test_ascii(self):
        self.assertEqual(readmes.github_anchor("Quick start"), "quick-start")

    def test_emoji_is_dropped_and_leaves_a_leading_hyphen(self):
        self.assertEqual(readmes.github_anchor("🧪 Testing"), "-testing")

    def test_cjk_letters_are_kept(self):
        self.assertEqual(readmes.github_anchor("🧪 测试"), "-测试")
        self.assertEqual(readmes.github_anchor("🧪 テスト"), "-テスト")

    def test_accents_are_kept(self):
        self.assertEqual(readmes.github_anchor("Segurança e Instalação"), "segurança-e-instalação")

    def test_punctuation_removed_hyphens_and_underscores_kept(self):
        self.assertEqual(readmes.github_anchor("A_b-c (d), e!"), "a_b-c-d-e")

    def test_double_space_gives_double_hyphen(self):
        self.assertEqual(readmes.github_anchor("a  b"), "a--b")

    def test_empty(self):
        self.assertEqual(readmes.github_anchor(""), "")

    def test_anchors_of_one_languages_section_titles_are_distinct(self):
        for code in CODES:
            anchors = [readmes.github_anchor(readmes.section_title(code, name)) for name, _ in readmes.SECTIONS if readmes.UI[code].get("s_" + name) or name == "screenshots"]
            self.assertEqual(len(anchors), len(set(anchors)), code)


class FigureTokenTests(unittest.TestCase):
    def test_token_matches_names_with_colon_dot_plus_dash(self):
        for name in ("vectors", "a:b", "a.b", "a+b", "a-b_c"):
            self.assertEqual(readmes.FACT_TOKEN.findall("x {{fact:%s}} y" % name), [name])

    def test_token_ignores_spaces_and_unclosed(self):
        self.assertEqual(readmes.FACT_TOKEN.findall("{{fact: vectors}} {{fact:vectors}"), [])

    def test_two_tokens_in_one_line(self):
        self.assertEqual(readmes.FACT_TOKEN.findall("{{fact:a}} and {{fact:b}}"), ["a", "b"])

    def test_facts_in_replaces_every_token(self):
        with mock.patch.object(readmes, "fact", side_effect=lambda name: {"a": "1", "b": "22"}[name]):
            self.assertEqual(readmes.facts_in("{{fact:a}}/{{fact:b}}/{{fact:a}}", "src"), "1/22/1")

    def test_facts_in_text_without_tokens_is_unchanged(self):
        self.assertEqual(readmes.facts_in("nothing here", "src"), "nothing here")

    def test_unknown_figure_is_an_error_naming_the_source(self):
        with mock.patch.object(readmes, "fact", side_effect=KeyError("zzz")):
            with self.assertRaises(SystemExit) as caught:
                readmes.facts_in("{{fact:zzz}}", "where.py")
        self.assertIn("where.py", str(caught.exception))
        self.assertIn("zzz", str(caught.exception))

    def test_unavailable_figure_is_an_error_never_a_guess(self):
        with mock.patch.object(readmes, "fact", side_effect=readmes.doc_facts.Unavailable("no source")):
            with self.assertRaises(SystemExit) as caught:
                readmes.facts_in("{{fact:vectors}}", "w")
        self.assertIn("no source", str(caught.exception))


class FigureWordsTests(unittest.TestCase):
    SAMPLES = {
        "vectors": ["12 conformance vectors", "1 conformance vector", "12 vectores de conformidad", "12 vecteurs de conformité", "12 vecteurs de conformite",
                    "12 vettori di conformità", "12 Konformitätsvektoren", "12 vetores de conformidade", "12个一致性向量", "12個の適合ベクター"],
        "openapi_operations": ["40 operations", "40 operaciones", "40 opérations", "40 operazioni", "40 Operationen", "40 operações", "40 operacoes", "40 个操作", "40 操作"],
        "openapi_paths": ["30 HTTP paths", "30 paths", "30 rutas HTTP", "30 chemins", "30 percorsi", "30 HTTP-Pfade", "30 caminhos HTTP", "30 条路径"],
    }

    def test_each_language_phrase_is_recognised(self):
        for kind, samples in self.SAMPLES.items():
            pattern = re.compile(r"(\d+)\s*" + readmes.FIGURE_WORDS[kind])
            for sample in samples:
                self.assertIsNotNone(pattern.search(sample), f"{kind}: {sample}")

    def test_a_different_word_is_not_a_figure(self):
        pattern = re.compile(r"(\d+)\s*" + readmes.FIGURE_WORDS["vectors"])
        self.assertIsNone(pattern.search("12 apples"))
        self.assertIsNone(pattern.search("conformance vectors"))


class CatalogEdgeTests(unittest.TestCase):
    def setUp(self):
        info = {"version": "1.2.3", "role": "Role", "maturity": "functional"}
        self.patch = mock.patch.object(make_catalog, "ROOT")
        root = self.patch.start()
        self.addCleanup(self.patch.stop)
        root.__truediv__ = lambda *_: mock.MagicMock(__truediv__=lambda *_: mock.MagicMock(read_text=lambda **k: json.dumps(info)))

    def test_table_has_header_separator_and_one_row_per_repository(self):
        rows = make_catalog.table().split("\n")
        self.assertEqual(rows[0], "| Repository | Version | Responsibility | Maturity |")
        self.assertEqual(rows[1], "|---|---|---|---|")
        self.assertEqual(len(rows), 2 + len(make_catalog.ORDER))
        self.assertTrue(all(row.count("|") == 5 for row in rows))

    def test_render_between_markers_keeps_head_and_tail(self):
        current = f"head\n{make_catalog.BEGIN}\nold\n{make_catalog.END}\ntail\n"
        out = make_catalog.render(current)
        self.assertTrue(out.startswith("head\n"))
        self.assertTrue(out.endswith("\ntail\n"))
        self.assertNotIn("\nold\n", out)

    def test_render_is_idempotent(self):
        first = make_catalog.render("x\n\n| Repository | a |\n|---|---|\n| r | 1 |\n\ny\n")
        self.assertEqual(make_catalog.render(first), first)

    def test_unknown_maturity_is_rejected(self):
        self.assertNotIn("legacy", make_catalog.MATURITY)
        self.assertEqual(sorted(make_catalog.MATURITY), ["established", "functional", "production", "scaffolding"])

    def test_maturity_colours_cover_the_same_levels(self):
        self.assertEqual(sorted(readmes.MATURITY_COLOR), sorted(make_catalog.MATURITY))


class PublicationEdgeTests(unittest.TestCase):
    def scan(self, text, where="a.txt"):
        findings = []
        check.scan_text("REPO", where, text, findings)
        return findings

    def test_public_ip_edges(self):
        for ok in ("8.8.8.8", "1.1.1.1"):
            self.assertTrue(check.public_ip(ok), ok)
        for no in ("10.0.0.1", "172.16.0.1", "127.0.0.1", "169.254.1.1", "224.0.0.1", "256.1.1.1", "1.2.3", "", "::1"):
            self.assertFalse(check.public_ip(no), no)

    def test_public_ipv6_is_global(self):
        self.assertTrue(check.public_ip("2606:4700:4700::1111"))

    def test_private_ip_is_not_reported(self):
        self.assertEqual(self.scan("host 192.168.0.180 port 1883"), [])

    def test_ip_after_the_word_version_is_not_reported(self):
        self.assertEqual(self.scan("version 8.8.8.8"), [])

    def test_ip_with_out_of_range_octet_is_not_reported(self):
        self.assertEqual(self.scan("value 999.1.1.1"), [])

    def test_own_public_email_is_allowed_other_blocks(self):
        self.assertEqual(self.scan("write to electrohobby3d@gmail.com"), [])
        found = self.scan("write to someone@outlook.com")
        self.assertEqual(found[0][0], "BLOCK")
        self.assertNotIn("someone@outlook.com", found[0][3])

    def test_company_domains_are_not_personal_mailboxes(self):
        self.assertEqual(self.scan("contact team@example.org"), [])

    def test_email_case_is_ignored_for_the_allowed_one(self):
        self.assertEqual(self.scan("ElectroHobby3D@Gmail.com"), [])

    def test_private_key_header_blocks(self):
        found = self.scan("-----BEGIN RSA " + "PRIVATE KEY-----")
        self.assertEqual([item[3] for item in found], ["private key"])

    def test_fake_key_body_in_a_test_is_not_a_key(self):
        self.assertEqual(self.scan("-----BEGIN " + "PRIVATE KEY----- abcdefghijklmnopqrstuvwxyz"), [])

    def test_line_longer_than_2000_chars_is_skipped(self):
        self.assertEqual(self.scan("x@gmail.com " + "a" * 2100), [])

    def test_empty_and_blank_text(self):
        self.assertEqual(self.scan(""), [])
        self.assertEqual(self.scan("\n\n   \n"), [])

    def test_line_number_is_reported(self):
        found = self.scan("ok\nok\nname@yahoo.es")
        self.assertTrue(found[0][2].endswith(":3"))

    def test_finding_never_prints_the_whole_secret(self):
        found = self.scan("password = 'Zq9!xLmN3pRt7Wv'")
        for item in found:
            self.assertNotIn("Zq9!xLmN3pRt7Wv", item[3])

    def test_bad_path_without_content_is_bad(self):
        self.assertTrue(check.is_bad_path(".env"))
        self.assertFalse(check.is_bad_path("README.md"))

    def test_conformance_vector_needs_both_path_and_prefix(self):
        self.assertFalse(check.is_conformance_vector("src/main.py", "anything"))
        self.assertFalse(check.is_conformance_vector("conformance/v.json", "zzzzz"))

    def test_scan_bytes_ignores_clean_binary_and_empty(self):
        for data in (b"", b"\x00\x01\x02" * 100):
            findings = []
            check.scan_bytes("R", "f.bin", data, findings)
            self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
