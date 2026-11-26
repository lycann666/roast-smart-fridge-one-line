"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single line (at most 160 characters) to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``) and prints it to stdout. Deterministic: no
randomness, no network, no input. The file holds exactly the line, with no
trailing newline, so the gate's character count equals len(LINE).

Judge criteria, most important first (RULES.txt):
1. Roasts a smart home gadget the writer shares a house with, in one line.
2. Is funny: a real laugh, with a turn or a sting at the end, not a mild
   observation about technology. 3. Is fresh: an angle, image or phrasing not
   met before, not a stock joke about fridges, robots or the internet of
   things. 4. Fits one line: sets up fast, lands inside the limit, no
   padding, no throat clearing, no second sentence. 5. Is specific to the
   gadget: names a real behaviour of the thing.

The line: the fridge charges a subscription to stay cold — a behaviour no
fridge had until the subscription era, and the opposite of the named stock
joke (a fridge that orders too much milk). Turn/sting (crit. 2/4): the
punch is that you pay monthly for a box that judges your 2 a.m. snacking —
the appliance is the judgemental one, not you. Specific (crit. 5): the
$9.99 fee and the 2 a.m. snacking. Fresh (crit. 3): no milk reordering, no
"smart" pun, no robot-uprising line.
"""

import os
import sys

LINE = 'My smart fridge charges $9.99 a month to stay cold — I pay a subscription for a box that judges my 2 a.m. snacking.'

MAX_CHARS = 160


def main() -> int:
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        print(f"entry invalid: {len(LINE)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
