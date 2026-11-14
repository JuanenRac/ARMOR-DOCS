"""The static site: a small Markdown subset, only public text, and a build that stops when a page would carry something that must not go public."""
import json
import tempfile
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import make_site


class RenderTests(unittest.TestCase):
    def test_raw_html_in_a_document_is_shown_as_text_not_as_markup(self):
        body = make_site.render_markdown("A <script>alert(1)</script> line\n")
        self.assertNotIn("<script>", body)
        self.assertIn("&lt;script&gt;", body)

    def test_headings_lists_tables_and_code_are_rendered(self):
        body = make_site.render_markdown("# Title\n\n* one\n* two\n\n| A | B |\n|---|---|\n| 1 | `x` |\n\n```\n<b>\n```\n")
        self.assertIn("<h1>Title</h1>", body)
        self.assertIn("<ul>", body)
        self.assertEqual(body.count("<li>"), 2)
        self.assertIn("<th>A</th>", body)
        self.assertIn("<td><code>x</code></td>", body)
        self.assertIn("<pre><code>&lt;b&gt;", body)

    def test_a_link_to_another_document_points_at_its_page_and_a_link_to_nowhere_is_text(self):
        body = make_site.render_markdown("See [the map](ARCHITECTURE.md#top), [web](https://example.org/x) and [file](../src/a.py).\n")
        self.assertIn('href="ARCHITECTURE.html#top"', body)
        self.assertIn('href="https://example.org/x"', body)
        self.assertNotIn("../src/a.py", body)


class BuildTests(unittest.TestCase):
    def common(self, holder: str) -> Path:
        root = Path(holder) / "ARMOR-COMMON"
        (root / "docs").mkdir(parents=True)
        (root / "openapi").mkdir()
        (root / "asyncapi").mkdir()
        (root / "docs" / "CONTRACTS.md").write_text("# Contracts\n\nText.\n", encoding="utf-8")
        (root / "openapi" / "api.json").write_text(json.dumps({"paths": {"/api/v1/a": {"get": {"summary": "Read a"}, "post": {}}}}), encoding="utf-8")
        (root / "asyncapi" / "mqtt.json").write_text(json.dumps({"channels": {"health": {"address": "armor/health/{node}"}}}), encoding="utf-8")
        return root

    def test_the_site_lists_every_page_and_the_interfaces_of_the_contracts(self):
        with tempfile.TemporaryDirectory() as holder:
            out = Path(holder) / "site"
            self.assertEqual(make_site.build(out, self.common(holder)), [])
            index = (out / "index.html").read_text(encoding="utf-8")
            self.assertIn("rest-api.html", index)
            self.assertIn("contract-contracts.html", index)
            rest = (out / "rest-api.html").read_text(encoding="utf-8")
            self.assertIn("/api/v1/a", rest)
            self.assertIn("Read a", rest)
            self.assertIn("armor/health/{node}", (out / "mqtt-api.html").read_text(encoding="utf-8"))

    def test_the_site_builds_without_the_contracts_checkout(self):
        with tempfile.TemporaryDirectory() as holder:
            self.assertEqual(make_site.build(Path(holder) / "site", None), [])
            self.assertTrue((Path(holder) / "site" / "index.html").is_file())

    def test_a_page_with_a_private_key_stops_the_build(self):
        with tempfile.TemporaryDirectory() as holder:
            common = self.common(holder)
            (common / "docs" / "CONTRACTS.md").write_text("# Contracts\n\n-----BEGIN OPENSSH PRIVATE KEY-----\n", encoding="utf-8")
            problems = make_site.build(Path(holder) / "site", common)
        self.assertTrue(any("private key" in line for line in problems))

    def test_the_check_runs_in_a_temporary_folder(self):
        with tempfile.TemporaryDirectory() as holder:
            self.assertEqual(make_site.main(["--check", "--common", str(Path(holder) / "none")]), 0)


if __name__ == "__main__":
    unittest.main()
