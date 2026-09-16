#!/usr/bin/env python3
"""Regression checks for the revised manuscript (stdlib only).

Focuses on the defects found in the 2026-09-16 developmental audit:
staged listings/dialogues that did not behave as the text claimed,
broken Appendix/Part references, the series build issues, and stale
links.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTERS = [
    "index.qmd",
    "copyright.qmd",
    "chapters/philosophy.qmd",
    "chapters/introduction.qmd",
    "chapters/ai-revolution.qmd",
    "chapters/intentional-prompting-principles.qmd",
    "chapters/six-step-methodology.qmd",
    "chapters/restate-and-identify.qmd",
    "chapters/work-by-hand.qmd",
    "chapters/pseudocode.qmd",
    "chapters/convert-to-code.qmd",
    "chapters/test-with-data.qmd",
    "chapters/intentional-prompting-patterns.qmd",
    "chapters/debugging-with-ai.qmd",
    "chapters/refactoring-strategies.qmd",
    "chapters/case-studies.qmd",
    "chapters/scaling-complexity.qmd",
    "chapters/teaching-learning.qmd",
    "chapters/future-directions.qmd",
    "acknowledgments.qmd",
    "about-author.qmd",
    "appendices/common-pitfalls.qmd",
    "appendices/glossary.qmd",
]

STALE_LINKS = (
    "michaelborck.dev",
    "michaelborck.education",
    "ship-it-python-in-production",
)


def skip_appledouble(paths):
    return [p for p in paths if not p.name.startswith("._")]


def chapter_text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


class ManuscriptChecks(unittest.TestCase):
    def test_no_stale_links(self):
        for name in CHAPTERS + ["README.md"]:
            text = (ROOT / name).read_text(encoding="utf-8")
            for target in STALE_LINKS:
                with self.subTest(file=name, target=target):
                    self.assertNotIn(target, text)

    def test_no_mermaid_diagrams(self):
        for name in CHAPTERS:
            with self.subTest(file=name):
                self.assertNotIn("{mermaid}", chapter_text(name))

    def test_no_stale_appendix_references(self):
        for name in CHAPTERS:
            text = chapter_text(name)
            for match in re.finditer(r"Appendix [A-Z]", text):
                with self.subTest(file=name, ref=match.group(0)):
                    self.fail(f"literal {match.group(0)} reference")

    def test_part_references_use_rendered_numbering(self):
        for name in CHAPTERS:
            text = chapter_text(name)
            for match in re.finditer(r"\bPart (\d+)\b", text):
                with self.subTest(file=name, ref=match.group(0)):
                    self.fail(
                        f"literal '{match.group(0)}' — use Part I-V names"
                    )

    def test_nonlocal_precedes_usage(self):
        text = chapter_text("chapters/convert-to-code.qmd")
        self.assertNotIn(
            "if current_length > max_length:\n                nonlocal",
            text,
        )
        self.assertIn("nonlocal start, max_length", text)

    def test_final_implementation_guards_each_parity(self):
        text = chapter_text("chapters/convert-to-code.qmd")
        self.assertNotIn("if remaining_chars * 2 + 1 <= max_length", text)
        self.assertIn("odd_potential", text)
        self.assertIn("even_potential", text)
        self.assertIn('"aa"', text)  # regression doctest for the "aa" bug

    def test_debugging_dialogue_is_reframed(self):
        text = chapter_text("chapters/test-with-data.qmd")
        self.assertIn("Check the Diagnosis Before Applauding the Fix", text)

    def test_no_false_expectations_in_tests(self):
        text = chapter_text("chapters/test-with-data.qmd")
        self.assertNotIn('"civilservice"', text)
        self.assertIn('"civiccenter"', text)
        self.assertIn('"bacababacab"', text)

    def test_binary_search_example_symptom_is_real(self):
        text = chapter_text("chapters/debugging-with-ai.qmd")
        self.assertIn("right = mid", text)
        self.assertNotIn("it returns -1 instead of 3", text)

    def test_download_links_are_site_absolute(self):
        config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
        for target in ("converse-python-partner-ai.pdf",
                       "converse-python-partner-ai.epub"):
            with self.subTest(target=target):
                self.assertIn(f"href: /{target}", config)
                self.assertNotIn(f"href: {target}", config)

    def test_source_encoding_is_utf8(self):
        paths = skip_appledouble(sorted(ROOT.glob("**/*.qmd")))
        for path in paths:
            if "_book" in path.parts or "_print_source" in path.parts:
                continue
            with self.subTest(file=str(path)):
                path.read_text(encoding="utf-8")


if __name__ == "__main__":
    unittest.main(verbosity=2)
