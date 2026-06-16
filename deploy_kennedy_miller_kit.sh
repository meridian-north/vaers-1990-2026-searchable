#!/bin/bash
# Deploy the Kennedy-Miller VAERS review kit to GitHub Pages.
# Run on your Mac (where gh auth + keychain live):  bash deploy_kennedy_miller_kit.sh
set -e

REPO_DIR="$HOME/vaers-1990-2026-searchable"
cd "$REPO_DIR"

# 1. clear ALL stale git locks (left by the sandbox, which couldn't unlink them)
if pgrep -x git >/dev/null 2>&1; then
  echo "✗ a git process is actually running — close it (or any open editor/commit) and re-run." ; exit 1
fi
for L in .git/index.lock .git/HEAD.lock .git/config.lock .git/refs/heads/main.lock .git/ORIG_HEAD.lock; do
  [ -f "$L" ] && rm -f "$L" && echo "→ cleared stale $L"
done

# 2. confirm kit is present (already copied into the working tree)
if [ ! -f kennedy-miller-kit/kennedy_miller_vaers_review.html ]; then
  echo "✗ kennedy-miller-kit/ not found in repo — re-copy it first." ; exit 1
fi

# 3. verify the kit's own manifest before publishing
( cd kennedy-miller-kit && grep -v '^#' MANIFEST_SHA256.txt | shasum -a 256 -c ) \
  && echo "→ kit MANIFEST_SHA256 verified"

# 4. stage, commit, push
git add kennedy-miller-kit deploy_kennedy_miller_kit.sh
git commit -m "Add Kennedy-Miller VAERS review kit (six-axis corpus + webform)

Self-contained kit on the June 2026 removal of Miller (2021) vaccine-SIDS paper
from Toxicology Reports and the Kennedy transparency letter.
- kennedy_miller_vaers_review.html: interactive six-axis webform
- days-to-onset sample pull (VAERS 1990-2026, n=1,989,028): clustering is a
  reporting artifact present across all cohorts incl. non-fatal + baseline
- case-records corpus (Miller retained source_class=retracted), embedded caveats
- MANIFEST_SHA256 self-verifies. Neutral on safety, strong on method." \
  || echo "→ nothing new to commit"

# auth as the meridian-north account (same pattern as push_to_corpus.sh)
gh auth switch --user meridian-north 2>/dev/null || true
git push origin main

echo ""
echo "✓ Done. Live (allow ~1 min for Pages to rebuild):"
echo "  https://meridian-north.github.io/vaers-1990-2026-searchable/kennedy-miller-kit/kennedy_miller_vaers_review.html"
