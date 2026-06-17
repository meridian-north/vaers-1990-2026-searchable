#!/bin/bash
# Deploy the Kennedy-Miller VAERS review kit to GitHub Pages.
# Canonical source = ~/kennedy-miller-vaers-kit  → mirrored into the repo, manifest regenerated
# on the host (the sandbox can't always hash), then committed + pushed.
#   bash ~/vaers-1990-2026-searchable/deploy_kennedy_miller_kit.sh
set -e

REPO_DIR="$HOME/vaers-1990-2026-searchable"
SRC="$HOME/kennedy-miller-vaers-kit"
DEST="$REPO_DIR/kennedy-miller-kit"
cd "$REPO_DIR"

# 1. clear stale git locks (sandbox edits can't unlink them)
if pgrep -x git >/dev/null 2>&1; then
  echo "✗ a git process is running — close it (or any open editor/commit) and re-run." ; exit 1
fi
for L in .git/index.lock .git/HEAD.lock .git/config.lock .git/refs/heads/main.lock .git/ORIG_HEAD.lock; do
  [ -f "$L" ] && rm -f "$L" && echo "→ cleared stale $L"
done

# 2. remove any stray nested copy from an earlier sandbox sync
[ -d "$DEST/kennedy-miller-vaers-kit" ] && rm -rf "$DEST/kennedy-miller-vaers-kit" && echo "→ removed stray nested dir"

# 3. mirror the canonical kit into the repo (exact copy)
if [ ! -f "$SRC/kennedy_miller_vaers_review.html" ]; then
  echo "✗ canonical kit not found at $SRC" ; exit 1
fi
mkdir -p "$DEST"
rsync -a --delete --exclude '.git' "$SRC"/ "$DEST"/
echo "→ mirrored $SRC → $DEST"

# 4. regenerate the kit manifest on the host (authoritative hashes)
( cd "$DEST"
  { echo "# MANIFEST_SHA256 — Kennedy-Miller VAERS Review Kit (v2 + Miller steelman + kmv-011 SUID)"
    echo "# corpus: meridian-north pharmacovigilance · VAERS 1990-2026 (n=1,989,028)"
    echo "# generated: $(date -u +%Y-%m-%dT%H:%M:%SZ) · verify: grep -v '^#' MANIFEST_SHA256.txt | shasum -a 256 -c"
    echo "#"
    find . -type f ! -name 'MANIFEST_SHA256.txt' | sort | while read -r f; do shasum -a 256 "$f" | sed 's#  \./#  #'; done
  } > MANIFEST_SHA256.txt
  echo "→ regenerated MANIFEST_SHA256.txt"
  grep -v '^#' MANIFEST_SHA256.txt | shasum -a 256 -c >/dev/null && echo "→ manifest self-verifies"
)

# 5. stage, commit, push
git add kennedy-miller-kit deploy_kennedy_miller_kit.sh
git commit -m "Kit update: kmv-011 cross-national SUID (US vs Nordic, WHO MDB denominator)

- new tab + line chart: SUID per 100k live births, US vs 5 Nordics, composite R95+R99+W75
- US ~90-97 vs Nordic ~15-55, but similar schedules -> gap is sleep/certification/
  classification, NOT vaccine; ecological rate cannot isolate vaccination (stated)
- recorded-absence honesties shown: US denominator ends 2005; DK R99 recoding from 2007
- data/suid_crossnational_ok_rows.csv (gathered via kind-gatherer sweep, WHO MDB)
- manifest regenerated + self-verified" \
  || echo "→ nothing new to commit"

gh auth switch --user meridian-north 2>/dev/null || true
git push origin main

echo ""
echo "✓ Done. Live (~1 min for Pages):"
echo "  https://meridian-north.github.io/vaers-1990-2026-searchable/kennedy-miller-kit/kennedy_miller_vaers_review.html"
echo "  New tab: 'kmv-011 · US vs Nordic (denominator)'"
