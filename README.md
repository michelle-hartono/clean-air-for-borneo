# clean air for borneo

Tracker for the air purifiers funded by Michelle's 25th-birthday donations, going to
haze shelters in Palangka Raya, Central Kalimantan.

**Live:** https://michelle-hartono.github.io/clean-air-for-borneo/

That URL is the one printed on the thank-you cards. It must not change — don't rename
the repo, don't move the Pages source off `main` / `/ (root)`, don't add a CNAME.

## How it's wired

| File | What it is |
| --- | --- |
| `status.json` | The only file a status update touches. |
| `index.html` | Renders everything from `status.json`. Fetched at load, no build step. |
| `photos/` | Public photos, always added via `scripts/add_photo.py`. |
| `assets/hero.jpg` | The drawing at the top. |
| `.nojekyll` | Stops GitHub Pages running Jekyll over the files. |

Pages: Settings → Pages → Deploy from a branch, `main`, `/ (root)`. Redeploys about a
minute after each push.

## Updating

Open this folder in Claude Code and say things like `order placed`, `on the way`,
`received` with a photo, or `donations closed: NT$7,500, 2 purifiers`. See CLAUDE.md
for the full command list and the photo privacy rules.
