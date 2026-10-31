"""
Export the queue to a 3-tab spreadsheet.

    python3 scripts/export_xlsx.py                      -> ./DSA_Queue_HI.xlsx
    python3 scripts/export_xlsx.py --out ~/Desktop/x.xlsx

The repo is the source of truth; this file is a VIEW. Re-run it whenever you want
a fresh copy - never edit the spreadsheet and expect the repo to notice.

Tabs: Queue (every problem), Progress (live formulas), Patterns (recognition cues).

Needs openpyxl. If the system python refuses to install it (PEP 668), use a venv:
    python3 -m venv ~/.venvs/xlsx && ~/.venvs/xlsx/bin/pip install openpyxl
    ~/.venvs/xlsx/bin/python scripts/export_xlsx.py
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prep_lib as L

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.utils import get_column_letter
except ImportError:
    sys.exit("openpyxl is not installed. See the header of this file for the venv recipe.")

NAV, BAND, SUB = "1F3864", "2E5C8A", "EDF2FA"
DIFF = {"Easy": "E2EFDA", "Medium": "FFF2CC", "Hard": "FCE4E4"}
TIER = {"A": "C6E0B4", "B": "F2F2F2", "C": "FFFFFF", "D": "FCE4E4"}
SEC = {"01-two-pointers": "Two Pointers", "02-sliding-window": "Sliding Window",
 "03-prefix-sum": "Prefix Sum", "04-hashing-strings": "Hashing & Strings",
 "05-intervals": "Intervals", "06-stack": "Stack & Monotonic Stack",
 "07-linked-list": "Linked List", "08-binary-search": "Binary Search",
 "09-heap": "Heap & Top-K", "10-dfs-trees": "DFS on Trees",
 "11-dfs-graphs-matrices": "DFS on Graphs & Matrices", "12-bfs": "BFS",
 "13-backtracking": "Backtracking", "14-graphs-topo-shortest": "Topological Sort & Shortest Path",
 "15-union-find": "Union-Find", "16-trie": "Trie", "17-dynamic-programming": "Dynamic Programming",
 "18-greedy": "Greedy", "19-matrices": "Matrices", "20-design-ds": "Design a Data Structure",
 "21-bit-math": "Bit & Math"}
GAP = {"04-hashing-strings", "15-union-find", "20-design-ds", "21-bit-math"}
MAP = {"01-two-pointers": ["Two Pointers - opposite ends", "Two Pointers - fast & slow", "Dutch National Flag (3-way partition)"],
 "02-sliding-window": ["Sliding Window - variable size", "Sliding Window - fixed size"],
 "03-prefix-sum": ["Prefix Sum + HashMap", "Prefix Sum", "Kadane's Algorithm"],
 "04-hashing-strings": ["Hashing / Frequency Map", "Expand Around Centre"],
 "05-intervals": ["Merge Intervals / Sweep Line"], "06-stack": ["Monotonic Stack"],
 "07-linked-list": ["Linked List Reversal", "Dummy Node technique"],
 "08-binary-search": ["Binary Search - exact & bounds", "Binary Search on the ANSWER"],
 "09-heap": ["Top-K with a Heap", "Two Heaps (running median)", "K-way Merge"],
 "10-dfs-trees": ["Tree DFS (recursive)", "BST Inorder Property", "Lowest Common Ancestor", "Tree Construction from Traversals"],
 "11-dfs-graphs-matrices": ["Graph DFS / Connected Components"],
 "12-bfs": ["Graph BFS - shortest path (unweighted)", "Tree BFS (level order)", "Multi-source BFS"],
 "13-backtracking": ["Backtracking"], "14-graphs-topo-shortest": ["Topological Sort", "Dijkstra's Algorithm"],
 "15-union-find": ["Union-Find (Disjoint Set Union)"], "16-trie": ["Trie (Prefix Tree)"],
 "17-dynamic-programming": ["DP - 1D linear", "DP - Knapsack (0/1 and unbounded)", "DP - Grid",
                            "DP - Two strings (LCS family)", "DP - Longest Increasing Subsequence"],
 "18-greedy": ["Greedy - interval scheduling"], "19-matrices": ["In-place Index Marking"],
 "20-design-ds": ["LRU / LFU Cache", "O(1) Insert / Delete / GetRandom"],
 "21-bit-math": ["XOR Tricks", "Fast Exponentiation & Modular Arithmetic"]}

INDIA_NOTE = ("India = typical of Indian product/startup rounds (Zomato, Swiggy, CRED, Razorpay, "
 "Flipkart, PhonePe, Meesho, Groww, Zepto, Navi, Dream11). It is a RULE, not scraped data: "
 "Easy/Medium, tier A or B, in the core sections. Those rounds are 1-2 DSA interviews of standard "
 "problems plus LLD, and rarely reach Dijkstra, MST, bitmask DP or hard graph work.")

thin = Side(style="thin", color="D9D9D9")


def put(ws, cell, v, *, sz=9, b=False, color="000000", fill=None, wrap=False, link=None, top=False):
    c = ws[cell]; c.value = v
    c.font = Font(name="Arial", sz=sz, bold=b, color=color, underline=("single" if link else None))
    if fill: c.fill = PatternFill("solid", start_color=fill)
    c.alignment = Alignment(wrap_text=wrap, vertical=("top" if top else "center"))
    if link: c.hyperlink = link
    return c


def head(ws, title, sub, hdr):
    last = get_column_letter(len(hdr))
    for i, (h, w) in enumerate(hdr, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.merge_cells(f"A1:{last}1"); put(ws, "A1", title, sz=15, b=True, color="FFFFFF", fill=NAV)
    ws.merge_cells(f"A2:{last}2"); put(ws, "A2", sub, sz=10, color="404040", fill=SUB, wrap=True)
    ws.row_dimensions[2].height = 44
    for i, (h, _) in enumerate(hdr, 1):
        put(ws, f"{get_column_letter(i)}3", h, b=True, color="FFFFFF", fill=NAV, wrap=True)
    ws.row_dimensions[3].height = 28
    return last


def leetcode_url(row):
    m = re.search(r"https://leetcode\.com/problems/\S+", Path(row["file"]).read_text())
    return m.group(0).rstrip("/") + "/" if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(L.ROOT / "DSA_Queue_HI.xlsx"))
    a = ap.parse_args()

    rows = sorted([r for r in L.load() if r["order"] < 999], key=lambda r: r["order"])
    cues = {c["pattern"]: c for c in json.loads((L.ROOT / "scripts" / "pattern_cues.json").read_text())}
    wb = Workbook()

    # -------------------------------------------------------------- Queue
    ws = wb.active; ws.title = "Queue"
    last = head(ws, f"THE QUEUE  -  {len(rows)} PROBLEMS  -  pull-based, no dates",
        "Take the next unsolved row when you sit down. Nothing is scheduled; nothing is ever late. "
        "Tier A is the spine - do these even in a bad week; tier D is the least important work in its "
        "own section and is the first thing to drop. Sections marked (gap) are NOT on Hello "
        "Interview; they are added because the target companies ask them. Column H opens the lesson. "
        + INDIA_NOTE,
        [("Order", 6), ("Section", 24), ("#", 6), ("Problem  (click -> LeetCode)", 42), ("Diff", 8),
         ("Tier", 6), ("Asked at", 24), ("HI Lesson", 10), ("Status", 14), ("Date Solved", 12),
         ("Hints?", 8), ("Key insight / mistake", 44)])
    ws.freeze_panes = "E4"
    row, folder = 4, None
    for q in rows:
        if q["folder"] != folder:
            folder = q["folder"]
            n = sum(1 for x in rows if x["folder"] == folder)
            gap = "   (gap - not on Hello Interview)" if folder in GAP else ""
            ws.merge_cells(f"A{row}:{last}{row}")
            put(ws, f"A{row}", f"{SEC[folder].upper()}   |   {n} problems{gap}",
                sz=10, b=True, color="FFFFFF", fill=BAND)
            row += 1
        done = q["status"] == "done"
        put(ws, f"A{row}", q["order"]); put(ws, f"B{row}", SEC[q["folder"]]); put(ws, f"C{row}", q["number"])
        put(ws, f"D{row}", q["title"], color="0563C1", link=leetcode_url(q))
        put(ws, f"E{row}", q["difficulty"], b=True, fill=DIFF[q["difficulty"]])
        put(ws, f"F{row}", q["sheet"], b=True, color=NAV, fill=TIER[q["sheet"]])
        put(ws, f"G{row}", "" if q["asked"] == "-" else q["asked"])
        if q["lesson"]: put(ws, f"H{row}", "lesson", color="0563C1", link=q["lesson"])
        put(ws, f"I{row}", "Solved" if done else "Todo", fill=("FFF2CC" if done else None))
        put(ws, f"J{row}", str(q["solved_on"] or ""))
        put(ws, f"K{row}", "Yes" if q["hints"] == "Y" else ("No" if done else ""))
        put(ws, f"L{row}", "", wrap=True)
        for i in range(1, 13):
            ws[f"{get_column_letter(i)}{row}"].border = Border(bottom=thin)
        row += 1
    end = row - 1
    dv = DataValidation(type="list", formula1='"Todo,Solved,Solved w/ hint,Failed,Skipped"', allow_blank=True)
    ws.add_data_validation(dv); dv.add(f"I4:I{end}")
    dv2 = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
    ws.add_data_validation(dv2); dv2.add(f"K4:K{end}")
    ws.auto_filter.ref = f"A3:{last}{end}"

    # -------------------------------------------------------------- Progress
    ps = wb.create_sheet("Progress")
    head(ps, "PROGRESS  -  every number is a live formula",
        "Nothing to maintain here - change Status on the Queue tab and these update. There is "
        "deliberately no 'behind' count: this is a queue, not a calendar. Regenerate the whole file "
        "from the repo with scripts/export_xlsx.py.",
        [("", 28), ("Solved", 10), ("Total", 10), ("%", 10), ("", 4), ("Notes", 46)])
    solved = (f'COUNTIF(Queue!$I$4:$I${end},"Solved")+COUNTIF(Queue!$I$4:$I${end},"Solved w/ hint")')
    r = 4
    put(ps, f"A{r}", "OVERALL", sz=11, b=True, color="FFFFFF", fill=BAND); ps.merge_cells(f"A{r}:F{r}"); r += 1
    put(ps, f"A{r}", "All problems", b=True); put(ps, f"B{r}", f"={solved}")
    put(ps, f"C{r}", f"=COUNT(Queue!$A$4:$A${end})")
    put(ps, f"D{r}", f"=IFERROR(B{r}/C{r},0)").number_format = "0.0%"
    r += 2
    put(ps, f"A{r}", "BY TIER", sz=11, b=True, color="FFFFFF", fill=BAND); ps.merge_cells(f"A{r}:F{r}"); r += 1
    for t, note in (("A", "The spine. A bad week still does these."), ("B", "Normal sittings."), ("C", "Only if ahead.")):
        put(ps, f"A{r}", f"Tier {t}", b=True)
        put(ps, f"B{r}", f'=COUNTIFS(Queue!$F$4:$F${end},"{t}",Queue!$I$4:$I${end},"Solved")'
                         f'+COUNTIFS(Queue!$F$4:$F${end},"{t}",Queue!$I$4:$I${end},"Solved w/ hint")')
        put(ps, f"C{r}", f'=COUNTIF(Queue!$F$4:$F${end},"{t}")')
        put(ps, f"D{r}", f"=IFERROR(B{r}/C{r},0)").number_format = "0.0%"
        put(ps, f"F{r}", note, wrap=True); r += 1
    r += 1
    put(ps, f"A{r}", "BY TARGET", sz=11, b=True, color="FFFFFF", fill=BAND); ps.merge_cells(f"A{r}:F{r}"); r += 1
    for c, note in (("Amazon", ""), ("Google", ""), ("India", INDIA_NOTE)):
        put(ps, f"A{r}", c, b=True)
        put(ps, f"B{r}", f'=COUNTIFS(Queue!$G$4:$G${end},"*{c}*",Queue!$I$4:$I${end},"Solved")'
                         f'+COUNTIFS(Queue!$G$4:$G${end},"*{c}*",Queue!$I$4:$I${end},"Solved w/ hint")')
        put(ps, f"C{r}", f'=COUNTIF(Queue!$G$4:$G${end},"*{c}*")')
        put(ps, f"D{r}", f"=IFERROR(B{r}/C{r},0)").number_format = "0.0%"
        if note: put(ps, f"F{r}", note, wrap=True); ps.row_dimensions[r].height = 58
        r += 1
    r += 1
    put(ps, f"A{r}", "BY SECTION", sz=11, b=True, color="FFFFFF", fill=BAND); ps.merge_cells(f"A{r}:F{r}"); r += 1
    for f_ in sorted(SEC):
        nm = SEC[f_]
        put(ps, f"A{r}", nm, b=True)
        put(ps, f"B{r}", f'=COUNTIFS(Queue!$B$4:$B${end},"{nm}",Queue!$I$4:$I${end},"Solved")'
                         f'+COUNTIFS(Queue!$B$4:$B${end},"{nm}",Queue!$I$4:$I${end},"Solved w/ hint")')
        put(ps, f"C{r}", f'=COUNTIF(Queue!$B$4:$B${end},"{nm}")')
        put(ps, f"D{r}", f"=IFERROR(B{r}/C{r},0)").number_format = "0.0%"
        if f_ in GAP: put(ps, f"F{r}", "gap - not on Hello Interview")
        r += 1

    # -------------------------------------------------------------- Patterns
    pt = wb.create_sheet("Patterns")
    head(pt, f"PATTERNS  -  {len(SEC)} SECTIONS  -  recognise it in 60 seconds",
        "Recognition is what the first minute of an interview tests, and the Queue tab gives it away "
        "by grouping. Cover column B and read D: name the pattern before you look. "
        "The last columns count each section by tier - 'D skip' is the least important work in that "
        "section, safe to drop first without losing the pattern.",
        [("#", 5), ("Section", 26), ("HI Lesson", 11), ("RECOGNISE IT WHEN...", 50),
         ("THE INSIGHT", 50), ("Complexity", 24), ("Common mistake", 40),
         ("A", 5), ("B", 5), ("C", 5), ("D skip", 7), ("Total", 7)])
    pt.freeze_panes = "C4"
    r = 4
    for i, f_ in enumerate(sorted(SEC), 1):
        c = cues.get(MAP[f_][0], {})
        also = ", ".join(MAP[f_][1:])
        les = next((q["lesson"] for q in rows if q["folder"] == f_ and q["lesson"]), None)
        put(pt, f"A{r}", i, top=True)
        put(pt, f"B{r}", SEC[f_] + ("  (gap)" if f_ in GAP else ""), b=True, wrap=True, top=True)
        put(pt, f"C{r}", "lesson" if les else "-", color=("0563C1" if les else "808080"), link=les, top=True)
        put(pt, f"D{r}", c.get("recog", ""), wrap=True, top=True)
        put(pt, f"E{r}", c.get("insight", ""), wrap=True, top=True)
        put(pt, f"F{r}", c.get("cx", ""), wrap=True, top=True)
        put(pt, f"G{r}", c.get("mist", ""), wrap=True, top=True)
        sec_rows = [q for q in rows if q["folder"] == f_]
        for j, tier in enumerate("ABCD"):
            col = get_column_letter(8 + j)
            n = sum(1 for q in sec_rows if q["sheet"] == tier)
            put(pt, f"{col}{r}", n, top=True, b=(tier == "D"),
                fill=("FCE4E4" if tier == "D" and n else None))
        put(pt, f"L{r}", len(sec_rows), b=True, top=True)
        if also: put(pt, f"B{r+1}", f"also covers: {also}", sz=8, color="808080", wrap=True, top=True)
        pt.row_dimensions[r].height = 74
        for c_ in range(1, 9):
            pt[f"{get_column_letter(c_)}{r+1}"].border = Border(bottom=thin)
        r += 2

    md = ["# The sheet", "",
          f"{len(rows)} problems in one order. **Pull-based: take the next one when you sit down.**",
          "Nothing here is scheduled to a date and nothing is ever late - a dead week costs",
          "position, not progress. That is why the old 454-problem calendar died at 5 solved.", "",
          "| tier | meaning | count |", "|---|---|---|"]
    for tier, meaning in (("A", "the spine - a bad week still does these"),
                          ("B", "core - normal sittings"),
                          ("C", "useful depth - only if ahead"),
                          ("D", "**least important in its section - drop these first**")):
        md.append(f"| **{tier}** | {meaning} | {sum(1 for r in rows if r['sheet'] == tier)} |")
    md += ["", "Within a section the order is A -> B -> C -> D, easiest first, so working top-down",
           "always does the important problems before the optional ones.", "",
           "Run `python3 scripts/plan.py` rather than reading this top to bottom.", ""]
    for folder in sorted(SEC):
        s = [r for r in rows if r["folder"] == folder]
        les = next((r["lesson"] for r in s if r["lesson"]), None)
        counts = " · ".join(f"{t}:{sum(1 for r in s if r['sheet'] == t)}" for t in "ABCD")
        md += [f"## {SEC[folder]}" + ("  **(gap)**" if folder in GAP else ""), "",
               (f"Lesson: {les}" if les else "No Hello Interview lesson - added to patch a gap."),
               "", f"`{len(s)} problems  —  {counts}`", "",
               "| # | problem | diff | tier | asked at |", "|---|---|---|---|---|"]
        for r in s:
            md.append(f"| {r['order']:03d} | [{r['number']}. {r['title']}]({r['file']}) | "
                      f"{r['difficulty']} | {r['sheet']} | {'' if r['asked'] == '-' else r['asked']} |")
        md.append("")
    (L.ROOT / "SHEET.md").write_text("\n".join(md))

    out = Path(a.out).expanduser()
    wb.save(out)
    print(f"wrote {out}\nwrote {L.ROOT / 'SHEET.md'}")
    print(f"  Queue    {len(rows)} problems, rows 4-{end}")
    print(f"  Progress live formulas (blank until Excel opens and recalculates)")
    print(f"  Patterns {len(SEC)} sections")


if __name__ == "__main__":
    main()
