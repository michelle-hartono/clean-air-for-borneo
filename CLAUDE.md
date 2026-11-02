# Purifier tracker

A static page on GitHub Pages that follows the air purifiers bought with Michelle's 25th-birthday donations, from Taipei to haze shelters in Central Kalimantan. Friends reach it through a QR code printed on thank-you cards, so the URL must never change and the page must always load.

**Live URL (pinned — this is what the QR code points at):**
<https://michelle-hartono.github.io/clean-air-for-borneo/>

- `index.html` renders everything from `status.json`. Don't edit `index.html` for routine updates.
- `status.json` is the only file that changes for a status update.
- Photos live in `photos/` and are always added through `scripts/add_photo.py`.

## How the page reacts to the data

The design is driven by `status.json`, so getting the data right is the whole job:

- The drawing at the top sits under a layer of haze that thins as steps are completed,
  and is fully clear once every step of every shelter is done. The caption under it
  ("2 of 4") and the blue thread down the step rail come from the same count.
- The step a shelter is up to next is whichever one is first with `done: false` — it
  gets the pulsing ring and the line "Happening next."
- Optional: `raised.donors` (a number) makes the tally read "Raised from 23 of you"
  instead of just "Raised". Leave it out and the page simply omits it. Never a name,
  only a count.
- While donations are open, `raised.goal_purifiers` shows as "Goal · 2 air purifiers".

## Open questions — confirm before filling these in

- **The purifiers are Midea**, the model the shelter already uses, bought from an
  Indonesian Shopee listing that includes a filter. No price has been given yet, so
  `purifiers.planned` and `.spent` stay `null`.
- **Currency is unsettled.** `budget.currency` is TWD and the page prints `NT$`, but an
  Indonesian listing prices in IDR. Don't mix the two in one receipt — ask Michelle for
  the TWD figure, or for permission to show that line in IDR, before writing a number.
- **Who buys is unsettled.** If the shelter buys locally rather than Michelle shipping
  from Taipei, the step notes and the "Taipei → Palangka Raya" route line need rewording:
  the money and the banner travel that distance, the purifiers don't.

## Money: the "Where it goes" receipt

`budget.items` is the public account of what the donations paid for. Donors read this,
so it has to be true before it is tidy.

- Two lines are committed from the start: **air purifiers** and **sending the banner**
  (the one drawn at the birthday picnic, posted Taipei → Palangka Raya for the kids).
- Masks and spare filters get added *only* out of surplus — once the total is in and the
  purifiers and banner are paid for, whatever is left decides whether they go on the list
  at all. Don't list a thing she hasn't decided to buy.
- Each item has `planned` (an estimate) and `spent` (what actually left the bank).
  The page shows `spent` when it exists, otherwise `planned` tagged **est**, otherwise
  "to be costed". Both null is fine and renders honestly — don't fill a number in to
  make the row look finished.
- **Never invent or round a price.** If Michelle hasn't said what something cost, it
  stays null. A wrong number here is worse than a blank one.
- The stacked bar, the totals and the "still to allocate" line are all computed from
  these values and `raised.twd`. Don't hand-write a total.
- If spending ever goes past what was raised, the page says "Over budget". That branch is
  a safety net and shouldn't fire — donations came in above target. Don't pad `raised.twd`
  to hide it if it ever does.
- Amounts are plain integers in TWD, no separators: `5400`, not `"NT$5,400"`.

## Commands

Michelle will say short things like the ones below. Map them to `status.json` edits, set `"updated"` to today's date (YYYY-MM-DD, Taipei time), then validate, commit and push.

| Michelle says | What to change |
| --- | --- |
| `donations closed: NT$X, N purifiers` | `raised.closed = true`, `raised.twd = X`, `raised.purifiers = N`, `raised.date = today` |
| `donations closed: NT$X, N purifiers, M friends` | the above, plus `raised.donors = M` |
| `order placed` (+ what was ordered) | step `ordered`: `done = true`, `date = today`, note listing the items and quantities — **no prices** — in the shape "Two \<model\>, \<where it's going\>." Include masks and filters in the same sentence if they were in the order. Never guess a model: use the one Michelle actually names. |
| `on the way` (+ optional ETA) | step `shipped`: done, date, note like "Arriving around 28 November." |
| `received` (+ photo) | step `received`: done, date, note, photo |
| `switched on` / `installed` (+ photo) | step `installed`: done, date, note, photo |
| `add shelter: NAME, PLACE` | append a new shelter with the same four steps, all `done: false` |
| `add moment: TEXT` (+ optional photo) | append to `moments` with today's date |
| `goal: N purifiers` | `raised.goal_purifiers = N` |
| `cost: ITEM = NT$X` | that `budget.items` entry: `planned = X` (an estimate) |
| `spent: ITEM = NT$X` | that entry: `spent = X` (actually bought) |
| `add cost: LABEL` (+ optional NT$X) | append a `budget.items` entry, amounts null unless given |
| `drop cost: ITEM` | remove that `budget.items` entry |
| `undo last` | `git revert` the most recent tracker commit and push |

If a command doesn't say which shelter, use the first one (`ra-annisa`). If there are two shelters and it's ambiguous, ask.

Write notes in plain, warm, lowercase-friendly English, one or two sentences, for example: "Ordered on Shopee and shipping straight to the shelter." Every photo needs a short `alt` describing what's in it.

**Money stays in the receipt, goods stay in the step notes.** A step note says *what* was
ordered and how many — never a price, never a total. The "Where it goes" section is the
only place amounts appear, so the two never disagree and nobody has to read a number twice.

## Photos: privacy rules (always)

1. Run every photo through the script, never copy it in directly:
   `python3 scripts/add_photo.py <source> photos/<yyyy-mm-dd>-<step>.jpg [--blur x1,y1,x2,y2 ...]`
   The script strips EXIF/GPS metadata, resizes, and blurs boxes.
2. **Don't publish the Shopee order screenshot.** It carries the shelter's street address
   — a kindergarten — plus a phone number, recipient name, and order and tracking numbers,
   and the repo is public, so a committed image stays in git history even after it's
   removed. Name the model and unit price in the note instead: it's more checkable than a
   screenshot and costs nothing in privacy. If Michelle explicitly asks for it anyway,
   blur the address block, phone, name, and order and tracking numbers first.
3. Before saving, look at the image and blur anything that shouldn't be public: street addresses, phone numbers, recipient names, order or tracking numbers, bank details, QR codes or barcodes on parcels. Shopee screenshots always contain the address and phone number, so blur them.
4. Don't add photos where adults are shown on oxygen or in medical distress. Children's photos only if Michelle confirms Ranu Welum approved them.
5. Never put donor names, individual amounts, or bank details anywhere on the page.

## Before every push

- `python3 -m json.tool status.json > /dev/null` must pass.
- Every `photo` path in `status.json` must exist in `photos/`.
- Every `budget` amount is either `null` or a number Michelle actually gave you.
- Commit message: `tracker: <what changed>`, e.g. `tracker: order placed for RA Annisa`.
- Push to `main`. GitHub Pages redeploys in about a minute. Reply to Michelle with the live URL and a one-line summary of what changed.
