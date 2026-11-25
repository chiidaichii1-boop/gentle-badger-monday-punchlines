#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes a single original joke about Monday mornings to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, fully deterministic: the same bytes every run.
"""

import os


JOKE = (
    "Monday morning, my alarm clock quit its job \u2014 it said waking me up "
    "five days a week was inhumane, so now we just lie there, "
    "unemployed together."
)


def main():
    # The harness may provide an input dir; this entry needs no input
    # files, but honour the env var so the program follows the
    # standard entrypoint contract.
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR") or "/input"
    _ = input_dir
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
