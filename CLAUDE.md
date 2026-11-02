# Purifier tracker

A static page on GitHub Pages that follows the air purifiers bought with Michelle's 25th-birthday donations, from Taipei to haze shelters in Central Kalimantan. Friends reach it through a QR code printed on thank-you cards, so the URL must never change and the page must always load.

- `index.html` renders everything from `status.json`. Don't edit `index.html` for routine updates.
- `status.json` is the only file that changes for a status update.
- Photos live in `photos/` and are always added through `scripts/add_photo.py`.

## Commands

Michelle will say short things like the ones below. Map them to `status.json` edits, set `"updated"` to today's date (YYYY-MM-DD, Taipei time), then validate, commit and push.

| Michelle says | What to change |
| --- | --- |
| `donations closed: NT$X, N purifiers` | `raised.closed = true`, `raised.twd = X`, `raised.purifiers = N`, `raised.date = today` |
| `order placed` (+ optional screenshot) | step `ordered`: `done = true`, `date = today`, short note, photo if given |
| `on the way` (+ optional ETA) | step `shipped`: done, date, note like "Arriving around 28 November." |
| `received` (+ photo) | step `received`: done, date, note, photo |
| `switched on` / `installed` (+ photo) | step `installed`: done, date, note, photo |
| `add shelter: NAME, PLACE` | append a new shelter with the same four steps, all `done: false` |
| `add moment: TEXT` (+ optional photo) | append to `moments` with today's date |
| `undo last` | `git revert` the most recent tracker commit and push |

If a command doesn't say which shelter, use the first one (`ra-annisa`). If there are two shelters and it's ambiguous, ask.

Write notes in plain, warm, lowercase-friendly English, one or two sentences, for example: "Ordered on Shopee and shipping straight to the shelter." Every photo needs a short `alt` describing what's in it.

## Photos: privacy rules (always)

1. Run every photo through the script, never copy it in directly:
   `python3 scripts/add_photo.py <source> photos/<yyyy-mm-dd>-<step>.jpg [--blur x1,y1,x2,y2 ...]`
   The script strips EXIF/GPS metadata, resizes, and blurs boxes.
2. Before saving, look at the image and blur anything that shouldn't be public: street addresses, phone numbers, recipient names, order or tracking numbers, bank details, QR codes or barcodes on parcels. Shopee screenshots always contain the address and phone number, so blur them.
3. Don't add photos where adults are shown on oxygen or in medical distress. Children's photos only if Michelle confirms Ranu Welum approved them.
4. Never put donor names, individual amounts, or bank details anywhere on the page.

## Before every push

- `python3 -m json.tool status.json > /dev/null` must pass.
- Every `photo` path in `status.json` must exist in `photos/`.
- Commit message: `tracker: <what changed>`, e.g. `tracker: order placed for RA Annisa`.
- Push to `main`. GitHub Pages redeploys in about a minute. Reply to Michelle with the live URL and a one-line summary of what changed.
