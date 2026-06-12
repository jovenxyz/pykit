"""Strip markdown formatting and return plain text."""
from __future__ import annotations

import re

_CODE_BLOCK = re.compile(r"```[^\n]*\n.*?```", re.DOTALL)
_INLINE_CODE = re.compile(r"`([^`]+)`")
_IMAGE = re.compile(r"!\[([^\]]*)\]\([^)]+\)")
_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_REF_LINK = re.compile(r"\[([^\]]+)\]\[[^\]]*\]")
_BOLD = re.compile(r"\*\*([^*]+)\*\*|__([^_]+)__")
_ITALIC = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)|(?<!_)_([^_]+)_(?!_)")
_STRIKE = re.compile(r"~~([^~]+)~~")
_HEADER = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)
_BLOCKQUOTE = re.compile(r"^>\s?", re.MULTILINE)
_LIST_BULLET = re.compile(r"^\s*[-*+]\s+", re.MULTILINE)
_LIST_NUMBER = re.compile(r"^\s*\d+\.\s+", re.MULTILINE)
_HR = re.compile(r"^\s*[-*_]{3,}\s*$", re.MULTILINE)


def to_plain_text(markdown: str) -> str:
    """Return the plain-text equivalent of a markdown string."""
    text = markdown
    text = _CODE_BLOCK.sub(lambda m: _strip_fence(m.group(0)), text)
    text = _INLINE_CODE.sub(r"\1", text)
    text = _IMAGE.sub(r"\1", text)
    text = _LINK.sub(r"\1", text)
    text = _REF_LINK.sub(r"\1", text)
    text = _BOLD.sub(lambda m: m.group(1) or m.group(2), text)
    text = _ITALIC.sub(lambda m: m.group(1) or m.group(2), text)
    text = _STRIKE.sub(r"\1", text)
    text = _HEADER.sub(r"\1", text)
    text = _BLOCKQUOTE.sub("", text)
    text = _LIST_BULLET.sub("", text)
    text = _LIST_NUMBER.sub("", text)
    text = _HR.sub("", text)
    return text


def _strip_fence(block: str) -> str:
    lines = block.splitlines()
    if len(lines) <= 2:
        return ""
    return "\n".join(lines[1:-1])
