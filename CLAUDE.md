# Purifier tracker

A static page on GitHub Pages that follows the air purifiers bought with Michelle's 25th-birthday donations, from Taipei to haze shelters in Central Kalimantan. Friends reach it through a QR code printed on thank-you cards, so the URL must never change and the page must always load.

**Live URL (pinned — this is what the QR code points at):**
<https://michelle-hartono.github.io/clean-air-for-borneo/>

- `index.html` renders everything from `status.json`. Don't edit `index.html` for routine updates.
- The haze photographs and their captions live in `index.html`, not `status.json` — they're
  page furniture, like the drawing and the opening note.
- `status.json` is the only file that changes for a status update.
- Photos live in `photos/` and are always added through `scripts/add_photo.py`.

## How the page reacts to the data

The design is driven by `status.json`, so getting the data right is the whole job:

- The drawing at the top sits under a layer of haze that thins as steps are completed,
  and is fully clear once every step of every shelter is done. The caption under it
  ("2 of 4") and the blue thread down the step rail come from the same count.
- The step a shelter is up to next is whichever one is first with `done: false` — it
  gets the pulsing ring and the line "Happening next."
- `raised.twd` is the **total raised so far**, in both the open and closed states — the
  tally and the receipt both read it, so there is one number, never two that can disagree.
- `raised.seed` is Michelle's own starting amount. Her invitation says *"i'm starting us off
  with NT$3,000"*, so the page names her share separately in that language: "I started us
  off with NT$3,000. 7 friends have added NT$7,855 since." The friends' figure is
  **derived** as `twd - seed` — never store it, or the two will drift apart.
- `raised.donors` counts **friends only**, not Michelle. She is not one of the "you".
- While donations are open the receipt says "Raised so far" and shows the running surplus,
  because the leftover is what decides whether masks and filters happen.
- `credits` is the footer's photo credit, and it is **empty until a photograph actually
  arrives**. Don't credit anyone for a photo they haven't sent — Ranu Welum's pictures are
  expected when the purifiers reach the shelter, so add `"Ranu Welum Foundation"` (and
  `"Rumah Aman Asap"` if theirs) to `credits` in the same edit that adds the first photo,
  not before. The haze photographs carry their own credits in the captions.
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
- **Who buys is still open.** People in Indonesia can buy locally from the Indonesian
  Shopee listing, but Michelle may be able to order from Taiwan instead. Until she says,
  **write nothing about where the purifiers are bought or shipped from** — the item note is
  deliberately just "Two Midea units — the model the shelter already uses."
- **Price benchmark.** On 9 Nov 2026 the listing showed Rp2,299,000 per unit, with a
  six-hour flash sale at Rp1,768,000. Michelle chose to let the sale go and order after
  donations close on 16 November, so **expect roughly the Rp2,299,000 list price** (about
  NT$4,200 per unit at the time, ~NT$8,300 for two). Don't treat a figure near the list
  price as a mistake. This is a sanity check only — the receipt records the TWD that
  actually leaves her account, never a listing price.

## Money: the "Where it goes" receipt

`budget.items` is the public account of what the donations paid for. Donors read this,
so it has to be true before it is tidy.

- Two lines are committed from the start: **air purifiers** and **sending the banner**
  (the one drawn at the birthday picnic, posted Taipei → Palangka Raya for the kids).
- Masks and spare filters get added *only* out of surplus — once the total is in and the
  purifiers and banner are paid for, whatever is left decides whether they go on the list
  at all. Don't list a thing she hasn't decided to buy.
- An estimate can be a **range**: set `planned_low` and `planned_high` instead of `planned`
  and the line reads "NT$6,400–8,300 est". The totals and the bar use `planned_high`, the
  top of the range, so "Left over" is the *minimum* surplus and never overpromises. A real
  `spent` always wins and the range disappears.
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
| `donations so far: NT$X from N friends` | `raised.twd = X + raised.seed`, `raised.donors = N` (do the addition yourself; X is the friends' part) |
| `donations closed: NT$X, N purifiers` | `raised.closed = true`, `raised.twd = X`, `raised.purifiers = N`, `raised.date = today` |
| `donations closed: NT$X, N purifiers, M friends` | the above, plus `raised.donors = M` |
| `order placed` (+ what was ordered) | step `ordered`: `done = true`, `date = today`, note listing the items and quantities — **no prices** — in the shape "Two \<model\>, \<where it's going\>." Include masks and filters in the same sentence if they were in the order. Never guess a model: use the one Michelle actually names. |
| `on the way` (+ optional ETA) | step `shipped`: done, date, note like "Arriving around 28 November." |
| `received` (+ photo) | step `received`: done, date, note, photo |
| `switched on` / `installed` (+ photo) | step `installed`: done, date, note, photo |
| `add shelter: NAME, PLACE` | append a new shelter with the same four steps, all `done: false` |
| `add moment: TEXT` (+ optional photo) | append to `moments` with today's date |
| any command that adds the **first** photo | also add the photographer to `credits` |
| `goal: N purifiers` | `raised.goal_purifiers = N` |
| `cost: ITEM = NT$X` | that `budget.items` entry: `planned = X` (an estimate) |
| `cost: ITEM = NT$X to NT$Y` | that entry: `planned_low = X`, `planned_high = Y` (a range) |
| `spent: ITEM = NT$X` | that entry: `spent = X` (actually bought) |
| `add cost: LABEL` (+ optional NT$X) | append a `budget.items` entry, amounts null unless given |
| `drop cost: ITEM` | remove that `budget.items` entry |
| `undo last` | `git revert` the most recent tracker commit and push |

If a command doesn't say which shelter, use the first one (`ra-annisa`). If there are two shelters and it's ambiguous, ask.

Write notes in plain, warm, lowercase-friendly English, one or two sentences, for example: "Ordered on Shopee and shipping straight to the shelter." Every photo needs a short `alt` describing what's in it.

**Money stays in the receipt, goods stay in the step notes.** A step note says *what* was
ordered and how many — never a price, never a total. The "Where it goes" section is the
only place amounts appear, so the two never disagree and nobody has to read a number twice.

## Images from the internet: licence rules (always)

The page carries two documentary haze photographs in `assets/`, in the "The air it's going
into" section. Both were chosen because they are **freely licensed**, and that is the only
reason they are allowed to be there:

- `haze-sun.jpg` — Palangka Raya, 18 Aug 2026, by Yumiyumi9, **CC0 / public domain**.
- `haze-road.jpg` — southern national road, 29 Aug 2026, by ParadoxP P, **CC BY-SA 4.0**
  (attribution and a licence link are required, and are in the `<figcaption>` — don't
  remove them).

Rules for any future image:

1. **Never take an image off Google Images, Instagram, Facebook, or a stock site**
   (Alamy, iStock, Shutterstock, Getty, Dreamstime). Most results there are somebody's
   copyrighted work, stock agencies actively enforce, and this repo is public — a committed
   image stays in git history even after it's deleted.
2. Only use: Wikimedia Commons (check the licence on the file page), NASA/ESA imagery,
   Unsplash or Pexels, or something the photographer has given permission for.
3. Record author, licence and the source URL in the caption, not just the footer.
4. **Best source of all is Ranu Welum Foundation** — they are the partner, they have real
   photographs of this haze, and asking them is better than a stranger's picture.
5. Credit every photographer by the name they publish under, and never crop out a watermark.

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
- `credits` names only people who have actually sent a photograph.
- Open the page and confirm it still renders. Every `getElementById` in `index.html` must
  match an element that exists — a missing one throws and blanks the whole page.
- Commit message: `tracker: <what changed>`, e.g. `tracker: order placed for RA Annisa`.
- Push to `main`. GitHub Pages redeploys in about a minute. Reply to Michelle with the live URL and a one-line summary of what changed.
