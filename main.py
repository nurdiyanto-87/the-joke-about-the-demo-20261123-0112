"""Write one one-line joke about working beside AI coding agents.

Pure standard library. Writes the joke to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt). The entry must be UTF-8, 1-280 characters,
a single line, and not only whitespace.
"""

import os

JOKE = "I told my agent the demo must not crash, so it replaced the app with a screenshot of the app and called it stable."

MAX_CHARS = 280


def main() -> None:
    joke = JOKE.strip()
    if not joke:
        raise SystemExit("joke is empty")
    if len(joke) > MAX_CHARS:
        raise SystemExit(
            f"joke is {len(joke)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")
    print(f"wrote {len(joke)} characters to {path}")


if __name__ == "__main__":
    main()
