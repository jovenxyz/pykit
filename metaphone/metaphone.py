"""Metaphone phonetic algorithm (Lawrence Philips, 1990).

Maps an English word to a phonetic code so that similarly-pronounced words
share the same code. Pure-Python, no external data.
"""
from __future__ import annotations


_VOWELS = set("AEIOU")


def _is_vowel(c: str) -> bool:
    return c in _VOWELS


def metaphone(word: str) -> str:
    if not word:
        return ""
    w = "".join(ch for ch in word.upper() if ch.isalpha())
    if not w:
        return ""

    # ---- Initial-letter exceptions ----
    if w.startswith(("AE", "GN", "KN", "PN", "WR")):
        w = w[1:]
    elif w.startswith("X"):
        w = "S" + w[1:]
    elif w.startswith("WH"):
        w = "W" + w[2:]

    out = []
    i = 0
    n = len(w)

    def at(k: int) -> str:
        return w[k] if 0 <= k < n else ""

    while i < n:
        c = w[i]
        prev = at(i - 1)
        nxt = at(i + 1)
        nxt2 = at(i + 2)

        # skip duplicate letters (except for C)
        if c == prev and c != "C":
            i += 1
            continue

        if c in _VOWELS:
            if i == 0:
                out.append(c)
        elif c == "B":
            if not (i == n - 1 and prev == "M"):
                out.append("B")
        elif c == "C":
            if nxt == "I" and nxt2 == "A":
                out.append("X")
            elif nxt == "H":
                out.append("X")
                i += 2
                continue
            elif nxt in ("I", "E", "Y"):
                out.append("S")
            else:
                out.append("K")
        elif c == "D":
            if nxt == "G" and nxt2 in ("E", "I", "Y"):
                out.append("J")
                i += 3
                continue
            else:
                out.append("T")
        elif c == "F":
            out.append("F")
        elif c == "G":
            if nxt == "H":
                if i + 2 < n and not _is_vowel(at(i + 2)):
                    i += 2
                    continue
                else:
                    out.append("F")
                    i += 2
                    continue
            elif nxt == "N":
                i += 1
                continue
            elif nxt in ("E", "I", "Y"):
                out.append("J")
            else:
                out.append("K")
        elif c == "H":
            if _is_vowel(prev) and not _is_vowel(nxt):
                pass
            else:
                out.append("H")
        elif c == "J":
            out.append("J")
        elif c == "K":
            if prev != "C":
                out.append("K")
        elif c == "L":
            out.append("L")
        elif c == "M":
            out.append("M")
        elif c == "N":
            out.append("N")
        elif c == "P":
            if nxt == "H":
                out.append("F")
                i += 2
                continue
            else:
                out.append("P")
        elif c == "Q":
            out.append("K")
        elif c == "R":
            out.append("R")
        elif c == "S":
            if nxt == "H":
                out.append("X")
                i += 2
                continue
            elif nxt == "I" and nxt2 in ("O", "A"):
                out.append("X")
            else:
                out.append("S")
        elif c == "T":
            if nxt == "H":
                out.append("0")
                i += 2
                continue
            elif nxt == "I" and nxt2 in ("O", "A"):
                out.append("X")
            else:
                out.append("T")
        elif c == "V":
            out.append("F")
        elif c == "W":
            if _is_vowel(nxt):
                out.append("W")
        elif c == "X":
            out.append("KS")
        elif c == "Y":
            if _is_vowel(nxt):
                out.append("Y")
        elif c == "Z":
            out.append("S")

        i += 1

    return "".join(out)
