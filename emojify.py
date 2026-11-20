"""Turn every emoji in the built HTML into a small Twemoji SVG image.

Why: emoji are drawn by the reader's own system font. Older Windows 10,
older Android and some Linux/Chromebook setups do not have the newer emoji
(🫁 🫀 🫘 🪫 🫧 …) and show an empty rectangle (□) instead. An <img> looks the
same on every device and browser, in light and dark mode.

- The original emoji stays in the alt text, so copy/paste and screen readers
  still work.
- SVG files live in assets/emoji/ (only the ones the site uses).
- If a new chapter uses an emoji that is not in assets/emoji/ yet, the build
  downloads the pinned Twemoji package once (from the npm registry), adds the
  missing SVG to assets/emoji/ and carries on. Commit the new file afterwards.

Emoji graphics: Twemoji by Twitter, Inc. and contributors (jdecked fork),
licensed CC-BY 4.0 — https://github.com/jdecked/twemoji
"""
import io
import re
import tarfile
import urllib.request
from pathlib import Path

import emoji as emojilib

ROOT = Path(__file__).parent
EMOJI_DIR = ROOT / "assets" / "emoji"
TWEMOJI_VERSION = "15.0.0"
TWEMOJI_URL = f"https://registry.npmjs.org/@twemoji/svg/-/svg-{TWEMOJI_VERSION}.tgz"
CACHE = ROOT / ".cache" / f"twemoji-svg-{TWEMOJI_VERSION}.tgz"

USED = {}       # emoji char -> file code (for the search script)
MISSING = set()
_tar = None

FE0E, FE0F, ZWJ = "︎", "️", "‍"


def code_for(e):
    """Twemoji file name rule: drop FE0F unless the sequence has a ZWJ."""
    s = e if ZWJ in e else e.replace(FE0F, "")
    return "-".join(f"{ord(c):x}" for c in s)


def _from_package(code):
    global _tar
    if _tar is None:
        if not CACHE.exists():
            CACHE.parent.mkdir(parents=True, exist_ok=True)
            print(f"emoji: downloading Twemoji {TWEMOJI_VERSION} (one time)…")
            CACHE.write_bytes(urllib.request.urlopen(TWEMOJI_URL, timeout=60).read())
        _tar = tarfile.open(fileobj=io.BytesIO(CACHE.read_bytes()), mode="r:gz")
    try:
        return _tar.extractfile(f"package/{code}.svg").read()
    except KeyError:
        return None


def ensure(e):
    """Return the file code if an SVG exists (fetching it if needed), else None."""
    code = code_for(e)
    f = EMOJI_DIR / f"{code}.svg"
    if not f.exists():
        data = None
        try:
            data = _from_package(code)
        except Exception as ex:  # offline etc.
            print(f"emoji: could not download Twemoji ({ex})")
        if not data:
            MISSING.add(e)
            return None
        EMOJI_DIR.mkdir(parents=True, exist_ok=True)
        f.write_bytes(data)
        print(f"emoji: added assets/emoji/{code}.svg for {e}")
    USED[e] = code
    return code


def _matches(text):
    """Yield (start, end, emoji) for emoji that a browser would draw as emoji.

    Skips plain text symbols such as ↔ or ↩︎ (no FE0F, or with FE0E)."""
    for m in emojilib.emoji_list(text):
        e, a, b = m["emoji"], m["match_start"], m["match_end"]
        if b < len(text) and text[b] == FE0E:
            continue
        status = emojilib.EMOJI_DATA.get(e, {}).get("status", emojilib.STATUS["fully_qualified"])
        if status == emojilib.STATUS["unqualified"] and ord(e[0]) < 0x1F000:
            continue  # text-style symbol (↔, ↩, ©…) — leave as text
        yield a, b, e


def _img(e, root, cls="emoji"):
    code = ensure(e)
    if not code:
        return e
    return f'<img class="{cls}" draggable="false" alt="{e}" src="{root}assets/emoji/{code}.svg">'


def text(s, root):
    """Replace emoji in a plain text/HTML text fragment."""
    out, last = [], 0
    for a, b, e in _matches(s):
        out.append(s[last:a])
        out.append(_img(e, root))
        last = b
    out.append(s[last:])
    return "".join(out)


_SVG_TEXT = re.compile(r"<text\b([^>]*)>([^<]*)</text>")


def _svg_text(m, root):
    attrs, content = m.group(1), m.group(2)
    found = list(_matches(content))
    if not found:
        return m.group(0)
    rest = content
    for a, b, e in reversed(found):
        rest = rest[:a] + rest[b:]
    if rest.strip():
        # Emoji mixed with words inside one SVG label cannot become an image.
        # Fix in figures.py: put the emoji in its own <text class="emo"> element.
        print(f"emoji: WARNING — emoji inside SVG text with words: {content!r}")
        return m.group(0)
    get = lambda k, d: float((re.search(rf'\b{k}="([-\d.]+)"', attrs) or [None, d])[1])
    x, y = get("x", 0), get("y", 0)
    size = get("font-size", 24 if "emo" in attrs else 16)
    n = len(found)
    gap = size * 0.12
    total = n * size + (n - 1) * gap
    x0 = x - total / 2  # all diagram text is centered (text-anchor: middle)
    parts = []
    for i, (_, _, e) in enumerate(found):
        code = ensure(e)
        if not code:
            return m.group(0)
        parts.append(f'<image href="{root}assets/emoji/{code}.svg" x="{x0 + i * (size + gap):.1f}" '
                     f'y="{y - size * 0.86:.1f}" width="{size:g}" height="{size:g}"><title>{e}</title></image>')
    return "".join(parts)


_SKIP_OPEN = re.compile(r"<(script|style|title|textarea|head)\b", re.I)


def page(h, root):
    """Convert all emoji in a full HTML page. Attributes, <head>, scripts and
    styles are left alone; emoji inside SVG <text> become SVG <image>."""
    h = _SVG_TEXT.sub(lambda m: _svg_text(m, root), h)
    out, i, skip, in_svg = [], 0, None, 0
    for tok in re.split(r"(<[^>]*>)", h):
        if tok.startswith("<"):
            low = tok.lower()
            if skip:
                if low.startswith(f"</{skip}"):
                    skip = None
            else:
                mo = _SKIP_OPEN.match(tok)
                if mo and not tok.endswith("/>"):
                    skip = mo.group(1).lower()
                elif low.startswith("<svg"):
                    in_svg += 1
                elif low.startswith("</svg"):
                    in_svg = max(0, in_svg - 1)
            out.append(tok)
        elif skip or in_svg:
            out.append(tok)
        else:
            out.append(text(tok, root))
    return "".join(out)


def report():
    if MISSING:
        print("emoji: no Twemoji image for: " + " ".join(sorted(MISSING)) + " (left as text)")
    print(f"emoji: {len(USED)} different emoji drawn as images")
