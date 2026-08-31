# Climate security weekly

A phone-first reading site for a weekly climate-security digest. Static files, no
server, no login. A Claude Code routine writes each week's digest as JSON, a GitHub
Action validates it and merges it, GitHub Pages serves it.

Week one (25 to 31 August 2026) is included so nothing is hypothetical.

## Setup

Roughly forty minutes. Steps 1 to 3 you do yourself; from step 4 Claude Code can help.

### 1. Put this on GitHub

Create a new **public** repository. Public matters: GitHub Pages on free accounts only
serves public repos, and a login-free site is what you asked for. Anyone with the URL
can read it. Nothing here is confidential, but decide that deliberately.

Upload these files, or from a terminal:

```bash
git init
git add .
git commit -m "Digest site, week one"
git branch -M main
git remote add origin https://github.com/YOUR-NAME/climate-digest.git
git push -u origin main
```

### 2. Turn on Pages

Repository Settings, then Pages. Under Build and deployment set Source to
"Deploy from a branch", branch `main`, folder `/ (root)`. Save.

A minute later the site is at `https://YOUR-NAME.github.io/climate-digest/`.
Open it on your phone. In Safari use Share, then Add to Home Screen.

### 3. Allow the Action to publish

Settings, then Actions, then General. Under Workflow permissions choose
"Read and write permissions". Without this the publish workflow cannot merge to `main`.

### 4. Install Claude Code

The native installer needs no Node.js. On Windows, in PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

On macOS or Linux:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Close the terminal and open a new one, then `claude --version` to check. Clone the
repository, `cd` into it, and run `claude`.

Node.js is only needed if you want to run `scripts/build.mjs` on your own machine. The
GitHub Action installs its own copy, so validation happens whether or not you have it.

It reads `CLAUDE.md` on start, so it already knows the repository's rules. Try:

> Read CLAUDE.md and routine/PROMPT.md, then explain back to me what happens when the
> weekly routine runs, and where it would break.

That is a useful first exercise: you find out whether the instructions are actually
clear before anything runs unattended.

### 5. Connect the repository to Claude Code on the web

In the terminal session run `/web-setup`. This grants cloud sessions access to clone
the repository.

### 6. Create the routine

Go to `claude.ai/code/routines`, create a routine:

- **Repository:** your `climate-digest` repo
- **Schedule:** weekly, Monday evening
- **Prompt:** `Follow the instructions in routine/PROMPT.md in this repository.`
- **Connectors:** Gmail, for the emailed copy
- **Recipient:** put the email address in the routine configuration, not in the
  repository. The repository is public.

Keeping the real prompt in the repository rather than in the routine configuration
means you can revise it with Claude Code, in version control, and see what changed.

Routines can only push to branches starting with `claude/`, which is why
`.github/workflows/publish.yml` exists: it validates the pushed branch and merges it to
`main`. Nothing reaches the site without passing the schema.

### 7. Watch the first run

Trigger the routine manually rather than waiting a week. Then check, in order: the
routine session for what it did, the Actions tab for whether validation passed, and the
site for whether the new week appears at the top.

If the routine pushed a branch but the Action failed, the digest did not validate. The
Action log names the exact field. That is the system working.

## Working on it locally

```bash
node scripts/build.mjs          # validate every digest, rebuild the index
python3 -m http.server 8000     # preview at http://localhost:8000
```

`file://` will not work: the reader fetches JSON.

## Adding a digest by hand

The fallback when the routine fails and you do not want to lose a week:

1. Write `data/digests/YYYY-MM-DD.json` following the schema.
2. `node scripts/build.mjs`
3. Commit and push to `main`.

## Icons

`icon-192.png` and `icon-512.png` are not included. Until you add them the site works
but the home-screen icon is a browser default. Ask Claude Code to generate a pair.
