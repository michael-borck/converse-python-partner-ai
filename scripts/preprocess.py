#!/usr/bin/env python3
"""
CPPA-specific print preprocessing hook.

Re-wraps code blocks inside callout boxes at a tighter width (45 chars)
since callout padding reduces available horizontal space in PDF.

Called by the standard book-publisher preprocessing pipeline AFTER
files have been copied to _print_source/ and standard wrapping (50 chars)
has been applied.
"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "_print_source"

CALLOUT_WRAP_WIDTH = 45


def wrap_line(line, max_width):
    """Word-wrap a single line, preserving leading whitespace."""
    if len(line) <= max_width:
        return [line]

    leading = ""
    for ch in line:
        if ch in " \t":
            leading += ch
        else:
            break
    content = line[len(leading):]

    words = content.split(" ")
    lines = []
    current = ""
    for word in words:
        test = current + (" " if current else "") + word
        if current and len(leading) + len(test) > max_width:
            lines.append(leading + current)
            current = word
        else:
            current = test
    if current:
        lines.append(leading + current)
    return lines


def process_file(path):
    with open(path) as f:
        text = f.read()

    lines = text.split("\n")
    result = []
    in_callout = False
    in_code = False
    changes = 0

    for line in lines:
        stripped = line.strip()

        # Track callout boundaries
        if stripped.startswith("::: {.callout"):
            in_callout = True
            result.append(line)
            continue
        if stripped == ":::" and in_callout:
            in_callout = False
            in_code = False
            result.append(line)
            continue

        # Track code blocks inside callouts
        if in_callout and stripped.startswith("```"):
            in_code = not in_code
            result.append(line)
            continue

        # Wrap long code lines inside callouts
        if in_callout and in_code and len(line) > CALLOUT_WRAP_WIDTH:
            wrapped = wrap_line(line, CALLOUT_WRAP_WIDTH)
            result.extend(wrapped)
            if len(wrapped) > 1:
                changes += 1
        else:
            result.append(line)

    if changes > 0:
        with open(path, "w") as f:
            f.write("\n".join(result))

    return changes


def main():
    if not OUTPUT_DIR.exists():
        print("  _print_source/ not found, skipping")
        return

    total = 0
    for qmd in sorted(OUTPUT_DIR.rglob("*.qmd")):
        changes = process_file(qmd)
        if changes > 0:
            rel = qmd.relative_to(OUTPUT_DIR)
            print(f"    Tightened {changes} code lines: {rel}")
            total += changes

    if total > 0:
        print(f"    Total: {total} lines re-wrapped at {CALLOUT_WRAP_WIDTH} chars")


if __name__ == "__main__":
    main()
