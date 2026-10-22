"""Every tool that keeps its own list of the repositories of the family names the same ones: a repository added to one list and forgotten in another is found here, not in a release."""
import re
import unittest
from pathlib import Path

import _support  # noqa: F401  (puts tools/ on the path)

import make_brand
import sync_ci_tools
from make_readmes import ORDER

ROOT = Path(__file__).resolve().parents[1]
FAMILY = ROOT.parent
NODES = {"ARMOR-RADAR", "ARMOR-SOLAR", "ARMOR-ELECTRICAL", "ARMOR-ALARM", "ARMOR-HMI"}


def readme_sources() -> set[str]:
    """The repositories that have a README source here: one file per repository in tools/readme_src/repos."""
    return {path.stem.replace("_", "-") for path in (ROOT / "tools" / "readme_src" / "repos").glob("ARMOR_*.py")}


class RegistryTests(unittest.TestCase):
    def test_the_readme_order_names_exactly_the_repositories_that_have_a_source(self):
        self.assertEqual(set(ORDER), readme_sources())
        self.assertEqual(len(ORDER), len(set(ORDER)), "a repository twice in the order")

    def test_the_brand_pictures_and_the_family_map_name_the_same_repositories(self):
        self.assertEqual(set(make_brand.REPOS), readme_sources())
        self.assertEqual(set(make_brand.POSITIONS), readme_sources())

    def test_the_tools_copied_into_each_repository_reach_every_repository_but_their_source(self):
        self.assertEqual(set(sync_ci_tools.TARGETS), readme_sources() - {"ARMOR-COMMON"})

    def test_the_script_that_checks_everything_runs_the_host_tests_of_all_five_nodes(self):
        script = (ROOT / "tools" / "check_all.sh").read_text(encoding="utf-8")
        loops = re.findall(r"for node in ([A-Z -]+); do", script)
        self.assertTrue(loops, "check_all.sh has no loop over the nodes")
        for loop in loops:
            self.assertEqual(set(loop.split()), NODES)

    def test_the_shared_firmware_goes_to_the_same_five_nodes(self):
        common = FAMILY / "ARMOR-COMMON" / "tools"
        if not common.is_dir():
            self.skipTest("ARMOR-COMMON is not next to this repository")
        text = (common / "sync_firmware_base.py").read_text(encoding="utf-8")
        block = text[text.index("PROJECTS = {"):]
        block = block[:block.index("\n}\n")]
        self.assertEqual(set(re.findall(r'"(ARMOR-[A-Z-]+)":', block)), NODES)
        tool = (common / "armor_project_tool.py").read_text(encoding="utf-8")
        listed = re.search(r"NODE_REPOSITORIES = \(([^)]*)\)", tool)
        self.assertEqual(set(re.findall(r'"(ARMOR-[A-Z-]+)"', listed.group(1))), NODES)


if __name__ == "__main__":
    unittest.main()
