# Unicode Emoji Proposals

Five emoji proposals prepared following the [Unicode Emoji Proposal Guidelines](https://www.unicode.org/emoji/proposals.html).

## Proposals

| # | Emoji | Name | Category | Key conflict addressed |
|---|---|---|---|---|
| 1 | Nail Biting | `nail-biting/` | People & Body — hand-fingers-partial | Distinct from 💅 nail polish and 🫦 biting lip |
| 2 | Whip | `whip/` | Objects — tool | No existing conflict; breaks new ground |
| 3 | Tail | `tail/` | Animals & Nature — animal-mammal | Standalone body part (like 🐽 pig nose, 🦴 bone) |
| 4 | Sharp Teeth | `sharp-teeth/` | People & Body — body-parts | Renamed from "fangs" to avoid overlap with 🧛 vampire |
| 5 | Bull Horns | `bull-horns/` | Animals & Nature — animal-mammal | Distinct from 🤘 sign of the horns (hand gesture) and ♉ Taurus (glyph) |

## Folder structure

```
unicode-reqs/
├── nail-biting/
│   ├── proposal.md          # Full proposal document
│   └── images/               # Color & B&W images at 18×18 and 72×72
├── whip/
│   ├── proposal.md
│   └── images/
├── tail/
│   ├── proposal.md
│   └── images/
├── sharp-teeth/
│   ├── proposal.md
│   └── images/
├── bull-horns/
│   ├── proposal.md
│   └── images/
├── data-collection/
│   └── frequency-evidence.md  # Google Search/Video/Trends/Ngram URLs for all 5
├── generate_artwork.py         # Python script to regenerate example images
└── README.md
```

## Fangs → Sharp Teeth rename

The original request was for a "fangs" emoji (with a "[costume]" hint). The 🧛
vampire emoji (U+1F9DB, Unicode 10.0) already has "fangs" as a CLDR keyword and
depicts fangs visually. A standalone "fangs" emoji would risk rejection under the
"Already Representable" exclusion factor.

**Resolution:** Renamed to "Sharp Teeth" — a broader, more descriptive term that:
- Avoids the "fangs" keyword overlap with the vampire emoji
- Encompasses monsters, predators, Halloween costumes, and aggressive expressions
- Follows the Unicode guideline preference for descriptive over prescriptive names

## Next steps before submission

1. **Capture screenshots:** Open each URL in `data-collection/frequency-evidence.md`
   in a private/incognito browser window and capture screenshots of:
   - Google Search (with result count visible via Tools button)
   - Google Video Search (with result count)
   - Google Trends: Web Search (elephant vs. term)
   - Google Trends: Image Search (elephant vs. term)
   - Google Books Ngram Viewer (elephant vs. term)

2. **Embed screenshots:** Insert the captured screenshots into each proposal's
   Frequency section.

3. **Convert to PDF:** Convert each `proposal.md` to PDF (required format for
   submission).

4. **Review against selection factors:** Verify each proposal addresses all
   Factors for Inclusion and Exclusion per the guidelines.

5. **Submit:** Provide a publicly accessible PDF link via the
   [Unicode Emoji Submission Form](https://forms.gle/6KSiYHrUdBkTMNaB8).

## Submission timeline

Per the Unicode guidelines (last updated 2026-08-11): submissions closed July 31,
2026 and will re-open in 2027. These proposals are prepared for the next
submission window.

## Artwork license

All example images are the submitter's original work, created programmatically
with Python/Pillow. The submitter owns all IP Rights and certifies the images are
suitable for incorporation into the Unicode Standard.
