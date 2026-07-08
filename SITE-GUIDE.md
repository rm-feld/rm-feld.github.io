# Running this site (cheatsheet)

This whole folder (`website/` in your vault) is the Quartz v5 repo — your
notes live in `content/`, right alongside the build tooling. Editing a file
in Obsidian *is* editing the tracked file; there's no separate copy/sync step.

## Everyday workflow

1. Edit/curate notes in Obsidian, inside `website/content/` (curate what's
   public by copying notes from your private vault into
   `website/content/vault/`).
2. From this folder, run:
   ```
   npx quartz sync
   ```
   This pulls, commits, and pushes. GitHub Actions rebuilds and redeploys
   automatically on push.
3. To preview locally before pushing:
   ```
   npx quartz build --serve
   ```
   then open http://localhost:8080.

## One-time setup (if you haven't already)

Obsidian will index `node_modules/`, `.quartz/`, `docs/`, and `public/` by
default since they're inside the vault now — worth excluding them in
Obsidian's Settings -> Files & Links -> Excluded files, so search/graph view
isn't cluttered with build artifacts:
```
website/node_modules
website/.quartz
website/docs
website/public
```
(None of these get committed to git either way — see `.gitignore`.)

## Where things live

- **Top nav** (Home / Vault / Research / Publications): hardcoded in
  `quartz/components/TopNav.tsx`. Edit the `navItems` array at the top of that
  file to add/remove/reorder tabs — `slug` should match the target file's path
  under `content/` (no `.md`, no leading slash).
- **Folder-scoped layout** (Explorer/Graph/Backlinks only inside `vault/`):
  in `quartz.ts`, see `isVaultPage` and the `ConditionalRender(...)` calls
  around `Explorer`/`Graph`/`Backlinks`. To change which folder gets the "full
  treatment," edit the `startsWith("vault/")` check.
- **Home page layout**: `content/index.md` (edit the text directly — the
  `<div class="home-hero">` / `home-hero__image` / `home-hero__text` wrapper
  around it doesn't need to change). Layout CSS is in
  `quartz/styles/custom.scss` under "Home page two-column hero."
- **Broken-wikilink styling**: enabled via `disableBrokenWikilinks: true` on
  the `crawl-links` plugin in `quartz.config.yaml`; the greyed-out look + hover
  tooltip text live in `quartz/styles/custom.scss` under "Broken wikilinks."
- **Colors/fonts/site title**: `quartz.config.yaml` -> `configuration` block.
- **Everything else** (adding/removing plugins, e.g. comments, analytics):
  `quartz.config.yaml` -> `plugins` list. See https://quartz.jzhao.xyz/configuration.

## Known caveats

- `og-image` (social share preview cards) is currently **disabled** in
  `quartz.config.yaml` — it fetches fonts from Google Fonts at build time,
  which the sandbox this was built in couldn't reach. GitHub Actions runners
  should have no trouble with this. Once your first deploy is live and
  working, try flipping it to `enabled: true`, push, and confirm the build
  still passes before relying on it.
- The headshot image referenced in `content/index.md`
  (`casual_headshot_jun26.jpeg`) needs to be placed in `content/` (same folder
  as `index.md`) — it wasn't available to copy automatically.
