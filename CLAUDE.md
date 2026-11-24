# Purifier tracker

A static page on GitHub Pages that follows the air purifiers bought with Michelle's 25th-birthday donations, from Taipei to haze shelters in Central Kalimantan. Friends reach it through a QR code printed on thank-you cards, so the URL must never change and the page must always load.

**Live URL (pinned — this is what the QR code points at):**
<https://michelle-hartono.github.io/clean-air-for-borneo/>

- `index.html` renders everything from `status.json`. Don't edit `index.html` for routine updates.
- The haze photographs and their captions live in `index.html`, not `status.json` — they're
  page furniture, like the drawing and the opening note.
- `status.json` is the only file that changes for a status update.
- Photos live in `photos/` and are always added through `scripts/add_photo.py`.

## The look comes from the invitation — don't invent a new one

Michelle's birthday invitation is the design system. The page was realigned to it on
9 Nov 2026 and should stay aligned:

- **Palette, sampled from the card:** paper `#F0ECE3`, ink `#3D3930`, and the brick red
  `#9E4B30` of *"i'm starting us off with NT$3,000."*
- **Red is her voice, never a state.** It marks the wish, links, the quote rule and the
  seed amount. Progress and completion read in moss `#6B7D54`. Never use red for an error,
  a warning or an overspend.
- **Forest tones are the dress code** — moss, olive, earth, sage, cream — and they colour
  the budget bar and the sources strip. Don't introduce a hue that isn't on the card.
- **Type is all DM Sans** (headlines lowercase, weight 500) with DM Mono for data: dates,
  amounts, labels. No serif, no display face.
- **Her devices:** headlines in quotes and lowercase; slash-delimited footer lines
  (`/ supporting Rumah Aman Asap · Ranu Welum Foundation /`); the goal written as the card
  writes it, "goal · two air purifiers for the shelter".
- The copy in the lede is adapted from the invitation's own body text. If the invitation
  wording changes, change the page to match, not the other way round. **Rumah Aman Asap
  Annisa stays named in that sentence** — it was the original ask. Later recipients are
  added around it ("You gave enough for other shelters nearby too"), never by replacing it
  with a generic plural.

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
- **Every bar carries a caption in words** (`.barkey` under it) saying what it shows. A bar
  that needs explaining out loud is decoration — if a change makes one unreadable, fix the
  bar or cut it, don't leave it bare.
- **There are two bars and they measure different axes.** The strip under the tally shows
  where the money *came from* (Michelle's seed, then friends). The split bar in "Where it
  goes" shows where it *is going* (per budget item, with the unspent remainder hatched).
  Her seed can never appear in the second one — it is a source, not a destination.
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

## Where things stand (last updated 24 Nov 2026)

**The money is closed and fully spent. Don't recalculate it — just don't break it.**

| | |
| --- | --- |
| Raised | **NT$17,397** = friends NT$14,321 + Michelle's seed NT$3,000 + her top-up NT$76 |
| Donations closed | 16 November 2026, 13 friends |
| Spent | **NT$17,397** — exactly level, the receipt reads "All of it spent" |

Eleven gifts came in NT$; two came in rupiah (Rp1,200,000 total) and are carried at the
market rate (~554 IDR/TWD = NT$2,166). Michelle paid for everything on her Taiwanese card
and reimburses herself from the rupiah held in her parents' Indonesian account.

**The three recipients**, one Xiaomi Smart Air Purifier 4 Lite and one spare filter each:

1. **Rumah Aman Asap RA Annisa** — a kindergarten turned haze shelter, Palangka Raya.
   The shelter from the invitation. NT$4,812, ordered 16 Nov.
2. **Panti Asuhan Ayah Bunda** — a children's home in Palangka Raya that also serves as a
   haze shelter. NT$4,813, ordered 19 Nov.
3. **GPdI Imanuel Kalahien** — a church in Kalahien that opens as a haze shelter.
   **Not in Palangka Raya.** NT$5,063, ordered 19 Nov.

Also bought: three spare filters (NT$2,259) and the banner's postage from Taipei (NT$450).

**Progress: 6 of 12 steps.** All three are "Order placed" and "On the way" as of 19 Nov.
What remains is `received` and `installed` for each — that's the whole job from here.

## Still open — ask, don't guess

- **No arrival dates yet.** Nothing on the page promises one; don't invent an ETA.
- **No photos yet**, so `credits` is empty. Ranu Welum's pictures are expected when the
  purifiers land. Add the photographer to `credits` in the same edit as the first photo.
- **The route line** in `index.html` still reads "Taipei → Palangka Raya · about 3,100 km",
  which no longer covers Kalahien. Michelle knows; she hasn't chosen a replacement.
- **The goal line** still says "two air purifiers for the shelter", matching the
  invitation, though three were bought. Left deliberately — her wording, her call.
- **Unit price ran NT$4,812–5,063.** The drift is the rupiah rate and the seller, not an
  error. Don't "correct" it.

## Hard-won rules about the money

- **Never infer an exchange rate from a price you were not given.** On 19 Nov a rate of
  490 IDR/TWD was derived by *assuming* a filter cost Rp369,000. The real rate was ~554.
  That error inflated the donation total by ~NT$283 and hid a genuine shortfall, and
  Michelle caught it, not the agent. Use the market rate on the day, or a rate she states.
- **Spending is whatever her card was actually charged in TWD** — that is what left her
  account. Don't convert a rupiah sticker price yourself and publish the result.
- **Value gifts and spending on the same basis.** Mixing a mid-market valuation of the
  gifts with a card-rate valuation of the spending once made the fund look over budget
  when it wasn't.
- **`raised.twd` = friends + `seed` + `topup`, and it equals the total spent.** If any one
  figure changes, recompute the others rather than editing one in isolation.

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
- When spending passes what was raised, the page says **"Topped up by me"** and the bar
  caption reads "All NT$X went out, and NT$Y more that I put in myself." That is now the
  live state, not a safety net. Never pad `raised.twd` to make it disappear.
- Amounts are plain integers in TWD, no separators: `5400`, not `"NT$5,400"`.

## Commands

Michelle will say short things like the ones below. Map them to `status.json` edits, set `"updated"` to today's date (YYYY-MM-DD, Taipei time), then validate, commit and push.

| Michelle says | What to change |
| --- | --- |
| `donations so far: NT$X from N friends` | *(historical — donations closed 16 Nov)* `raised.twd = X + seed + topup`, `raised.donors = N` |
| `donations closed: NT$X from N friends` | *(already done)* `raised.closed = true`, `raised.twd = X + seed + topup`, `raised.donors = N`, `raised.date = today` |
| `I put in another NT$X` | `raised.topup += X`, and add the same amount to `raised.twd` |
| `order placed` (+ what was ordered) | step `ordered`: `done = true`, `date = today`, note listing the items and quantities — **no prices** — in the shape "Two \<model\>, \<where it's going\>." Include masks and filters in the same sentence if they were in the order. Never guess a model: use the one Michelle actually names. |
| `on the way` (+ optional ETA) | step `shipped`: done, date, note like "Arriving around 28 November." |
| `received` (+ photo) | step `received`: done, date, note, photo |
| `switched on` / `installed` (+ photo) | step `installed`: done, date, note, photo |
| `add shelter: NAME, PLACE` | append a new shelter with the same four steps, all `done: false`. Word the `received` label for the place — "Received at the shelter" for a haze shelter, "Received at the home" for a children's home |
| `add moment: TEXT` (+ optional photo) | append to `moments` with today's date |
| any command that adds the **first** photo | also add the photographer to `credits` |
| `goal: N purifiers` | `raised.goal_purifiers = N` |
| `cost: ITEM = NT$X` | that `budget.items` entry: `planned = X` (an estimate) |
| `cost: ITEM = NT$X to NT$Y` | that entry: `planned_low = X`, `planned_high = Y` (a range) |
| `spent: ITEM = NT$X` | that entry: `spent = X` (actually bought) |
| `add cost: LABEL` (+ optional NT$X) | append a `budget.items` entry, amounts null unless given |
| `drop cost: ITEM` | remove that `budget.items` entry |
| `undo last` | `git revert` the most recent tracker commit and push |

There are **three** shelters now, so a bare command is usually ambiguous — **ask which
one** rather than defaulting. Only use `ra-annisa` without asking if the command clearly
refers to the original shelter.

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
6. Michelle will sometimes paste her working list of who has paid and how much. **That list
   never goes into this repo** — not the page, not a notes file, not a commit message. The
   repo is public and git history is permanent. Do the arithmetic outside the project and
   commit only the aggregate: `raised.twd`, `raised.seed`, `raised.donors`.

## Setting up on a different computer

Everything needed is in this repo. The steps once:

```
git clone https://github.com/michelle-hartono/clean-air-for-borneo.git
cd clean-air-for-borneo
python3 -m pip install --user Pillow     # only needed for scripts/add_photo.py
gh auth login                            # or: git config credential.helper
```

Check it works before trusting it:

```
python3 -m json.tool status.json         # must pass
python3 -c "import PIL; print(PIL.__version__)"
git log --oneline -1                     # should match github.com/michelle-hartono/clean-air-for-borneo
```

**If git or `gh` fails with "SSL certificate problem: unable to get local issuer
certificate", or `gh auth status` claims the token is invalid** — on macOS this is usually
a stale system CA bundle that can't chain to Sectigo's newer root, **not** a bad token and
**not** an attack. Point both at a current bundle:

```
git config http.sslCAInfo /opt/homebrew/etc/ca-certificates/cert.pem
export SSL_CERT_FILE=/opt/homebrew/etc/ca-certificates/cert.pem
```

(Adjust the path for the machine; `brew install ca-certificates` provides it.)
**Never disable certificate verification to get past this.**

Pages redeploys from `main` about a minute after each push. There is no build step — the
page fetches `status.json` at load, so a push is the whole deployment.

## Before every push

- `python3 -m json.tool status.json > /dev/null` must pass.
- Every `photo` path in `status.json` must exist in `photos/`.
- Every `budget` amount is either `null` or a number Michelle actually gave you.
- `credits` names only people who have actually sent a photograph.
- **Confirm the page still renders**, not just that the files look right. The whole page
  is drawn by JavaScript from `status.json`, so one bad reference blanks everything —
  and this URL is printed on thank-you cards. Serve it locally and check:

  ```
  python3 -m http.server 8080 &
  open http://localhost:8080          # or curl it and grep for "Where it goes"
  ```

  Every `getElementById` in `index.html` must match an element that exists.
- After pushing, fetch the live URL and confirm the change actually went out — Pages takes
  about a minute, so the first fetch often still shows the old version.
- Commit message: `tracker: <what changed>`, e.g. `tracker: order placed for RA Annisa`.
- Push to `main`. GitHub Pages redeploys in about a minute. Reply to Michelle with the live URL and a one-line summary of what changed.
