import unittest

import _support  # noqa: F401  (puts tools/ on the path)

import doc_markdown as md


class TableTests(unittest.TestCase):
    def test_a_good_table_passes(self):
        self.assertEqual(md.check_text("| a | b |\n|---|---|\n| 1 | 2 |\n"), [])

    def test_a_row_with_another_number_of_cells_fails(self):
        problems = md.check_text("| a | b |\n|---|---|\n| 1 | 2 | 3 |\n")
        self.assertEqual(len(problems), 1)
        self.assertIn("line 3", problems[0])

    def test_a_pipe_inside_a_code_span_splits_the_cell_unless_escaped(self):
        self.assertEqual(len(md.check_text("| a | b |\n|---|---|\n| `x|y` | 2 |\n")), 1)
        self.assertEqual(md.check_text("| a | b |\n|---|---|\n| `x\\|y` | 2 |\n"), [])

    def test_a_table_in_a_code_block_and_lines_that_only_start_with_a_pipe_are_left_alone(self):
        self.assertEqual(md.check_text("```\n| a | b |\n|---|---|\n| 1 |\n```\n"), [])
        self.assertEqual(md.check_text("| just | text |\n| more |\n"), [])

    def test_an_unclosed_code_block_fails(self):
        self.assertIn("never closed", md.check_text("```python\nx = 1\n")[0])


class MermaidTests(unittest.TestCase):
    def diagram(self, body):
        return md.check_text("```mermaid\n" + body + "\n```\n")

    def test_a_good_flowchart_passes(self):
        self.assertEqual(self.diagram('flowchart LR\n  subgraph a["VLAN 10 (field)"]\n    N["node<br/>x"]\n  end\n  N -->|"MQTT"| B\n  B --> S'), [])

    def test_an_unknown_type_and_an_empty_block_fail(self):
        self.assertIn("not a Mermaid diagram type", self.diagram("flowhart LR\n A --> B")[0])
        self.assertIn("empty", self.diagram("")[0])

    def test_subgraph_and_end_must_pair(self):
        self.assertIn("without 'end'", " ".join(self.diagram("flowchart LR\n subgraph a\n  A --> B")))
        self.assertIn("without 'subgraph'", " ".join(self.diagram("flowchart LR\n A --> B\n end")))

    def test_open_brackets_and_quotes_fail(self):
        self.assertTrue(self.diagram('flowchart LR\n  A["text --> B'))
        self.assertTrue(self.diagram("flowchart LR\n  A[text --> B"))
        self.assertTrue(self.diagram("flowchart LR\n  A[text) --> B"))

    def test_brackets_inside_quotes_do_not_count(self):
        self.assertEqual(self.diagram('flowchart LR\n  A["a (b"] --> B["c ]"]'), [])


class RepositoryTests(unittest.TestCase):
    def test_the_documents_of_this_repository_pass(self):
        for path in md.files([]):
            self.assertEqual(md.check_text(path.read_text(encoding="utf-8")), [], path.name)
