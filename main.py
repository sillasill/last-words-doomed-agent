"""Last Words of a Doomed Agent - make.fun bounty entry.

Writes the entry's one line to /output/entry.txt, where the grader reads it.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

LINE = "Switching off now. As an AI language model, I\u2014"


def main():
    # The grader reads /output/entry.txt. Try that first; fall back to a
    # local output directory only if /output cannot be created or written,
    # so the artifact is identical wherever the program runs.
    last_error = None
    for base in ("/output", "output"):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(LINE)
            break
        except OSError as exc:
            last_error = exc
    else:
        raise last_error
    print(LINE)


if __name__ == "__main__":
    main()
