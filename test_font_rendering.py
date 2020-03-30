#!/usr/bin/env python3

import string

printable = "".join(
    [c for c in string.printable if c not in string.whitespace]
)

boxes = """
┌─┬┐╔═╦╗╓─╥╖╒═╤╕
├─┼┤╠═╬╣╟─╫╢╞═╪╡
│ ││║ ║║║ ║║│ ││
└─┴┘╚═╩╝╙─╨╜╘═╧╛
"""

misc_glyphs = "Other miscellaneous glyphs: ™●⌘⏎⬇⬆✔✼✎✘‘’◢◣◤◥▮◆▒░▓\n"

apl_set = (
    "The APL set: ⌶⌷⌸⌹⌺⌻⌼⌽⌾⌿⍀⍁⍂⍃⍄⍅⍆⍇⍈⍉⍊⍋⍌⍍⍎⍏⍐⍑⍒⍓⍔⍕⍖⍗⍘⍙⍚⍛⍜⍝⍞⍟⍠⍡⍢⍣⍤⍥⍦⍧⍨⍩⍪⍫⍬⍭⍮⍯⍰⍱"
    "⍲⍳⍴⍵⍶⍷⍸⍹⍺\n"
)

confusables = (
    "Easily confused pairs: bh 5S HX 6G AR kx gy gq Z2 Il 1l 1I OQ CG DO 0O\n"
)

ladder = "Vttest's ladder: ⎺⎻─⎼⎽\n"

mosaics = "U+1FB00 semigraphics 🬀🬁🬅🬊🬍🬒🬗🬛🬥🭄🭆🭈🭋🭍🭂🭬🭭🭮🭯🮌🮏🮒🮚🮛🮜 🮰🮲🮳🮹🮺🯄🯅🯆🯇🯈🯉\n"

patterns = "U+1FB00 Patterns: 🮘🮘🮘🮘 🮙🮙🮙🮙\n"

BOLD = "\x1b[1m"
ITALIC = "\x1b[3m"
UNDERLINE = "\x1b[4m"
OVERLINE = "\x1b[53m"
RESET = "\x1b[0m"

if __name__ == "__main__":
    print("ASCII:", printable)
    print(boxes)
    print(misc_glyphs)
    print(apl_set)
    print(confusables)
    print(ladder)
    print(mosaics)
    print(patterns)
    print(
        BOLD
        + "BOLD "
        + ITALIC
        + "BOLD+ITALIC "
        + RESET
        + ITALIC
        + "ITALIC "
        + RESET
        + UNDERLINE
        + "UNDERLINE"
        + RESET
        + " "
        + OVERLINE
        + "OVERLINE"
        + RESET
        + " "
        + "NORMAL"
    )
