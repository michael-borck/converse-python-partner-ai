# Cover Design Ideas

*Saved for future reference - February 2026*

## Decision: Childlike Sketch Style

After exploring several directions (realistic, line art with watercolor, etc.), the **childlike pencil sketch on notebook paper** style emerged as the winner.

### Why This Style Works

- Instantly memorable and distinctive
- Approachable, non-intimidating (perfect for learning)
- Authentic and charming vs. AI-polished sterility
- Would stand out dramatically on Amazon
- Matches the "conversation" theme - like whiteboard/notebook sketches
- Ironic/meta: a book about AI with deliberately human, imperfect art
- Creates strong series identity

---

## Favorite Sample: #2 Style

The preferred direction features:
- Stick figure human with personality (smile, messy hair)
- Simple boxy robot (friendly, waving)
- Speech bubbles with scribbles inside
- **Lined notebook paper background with red margin line**
- Pencil sketch with optional crayon color accents

### What Made #2 Work

- Great balance of sketchy charm and professional usability
- The smile and messy hair give the human personality
- Robot is friendly (waving gesture)
- Notebook paper with red margin is distinctive and memorable
- Suggests "learning" and "notes from class"

---

## Series Unification Concept

All 5 books share:
- Same lined notebook paper background
- Same red margin line on left
- Same typography style for titles
- Different sketch for each book's unique concept

### Individual Book Concepts

| Book | Sketch Concept |
|------|----------------|
| **Converse Python, Partner AI** | Human + robot talking, speech bubbles connecting |
| **Think Python, Direct AI** | Human + robot, robot holding/showing a snake |
| **Code Python, Consult AI** | Human pointing at code on a board, robot watching |
| **Ship Python, Orchestrate AI** | Human + robot high-fiving, rocket doodle nearby |
| **Build Web, Guide AI** | Human + robot building something with blocks/web structure |

---

## Prompts That Worked (FLUX)

### Basic sketch style
```
Book cover, child's pencil drawing style, simple stick figure human on left
talking to stick figure robot on right, speech bubbles between them with
scribbles inside, wobbly hand-drawn lines, like a 5 year old drew it on
lined notebook paper, crayon and pencil texture, imperfect and charming,
white paper background with slight texture, naive art style, very simple
```

### With notebook paper (closer to #2)
```
Book cover, rough pencil sketch on lined notebook paper with red margin line,
stick figure person with messy hair and smile having conversation with simple
boxy robot who is waving, both drawn with shaky childlike lines, speech bubbles
with scribbles connecting them, doodle style, kindergarten drawing aesthetic,
wobbly imperfect lines, charming and naive, minimal detail
```

### With color accents
```
Book cover, child's drawing style on lined notebook paper, stick figure human
and simple robot facing each other talking, drawn in pencil with messy crayon
color fills, blue and yellow crayons, wobbly lines, red margin line visible,
naive art, like a kid explaining their day, imperfect and endearing, simple shapes
```

---

## Sample Files Generated

Located in `/Users/michael/Projects/books/`:
- `1.png` - Line art speech bubbles (rejected - too corporate)
- `2.png` - Line art speech bubbles variant (rejected)
- `11.webp` - Sketch style, clean
- `12.webp` - **FAVORITE** - Sketch with personality, notebook paper
- `13.webp` - "My Robot Friend" very childlike
- `14.png` - Overlapping speech bubbles, color, wide format
- `15.webp` - Minimal sketch style

---

## Next Steps (When Resuming)

1. Refine the #2 style further if needed
2. Generate consistent versions for all 5 books
3. Add title typography (clean sans-serif overlaid on sketch)
4. Create KDP-compliant versions (proper dimensions, spine for print)
5. Create matching assets for Gumroad/web

---

## Other Publishing Decisions Made

### Distribution
- Free online (Quarto site)
- Kindle ebook (Amazon, no ISBN needed)
- Paperback (Amazon KDP, use their free ISBN)
- PDF/EPUB (Gumroad and/or Itch.io, pay-what-you-want)

### Front/Back Matter Created
- `copyright.qmd` - Copyright page with cover art attribution, production notes
- `about-author.qmd` - Author bio and series list

### Cross-References
- All 5 books now consistently reference each other
- Series structure documented (Methodology → Python Track / Web Track)
- Ship Python, Orchestrate AI: "Professional Python in the AI Era" (renamed from "Ship It")

### KDP Settings
- PDF configured for 6"x9" trim size
- Margins set for binding (1" inner gutter)
- 11pt font size
