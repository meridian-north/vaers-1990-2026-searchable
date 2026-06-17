#!/bin/bash
# Publish the 5-Minute VAERS demo to GitHub Pages.
#   bash ~/vaers-1990-2026-searchable/deploy_five_minute_vaers.sh
# Mirrors ~/five-minute-vaers/{index.html,README.md} into the repo, commits, pushes.
set -e

REPO_DIR="$HOME/vaers-1990-2026-searchable"
SRC="$HOME/five-minute-vaers"
DEST="$REPO_DIR/five-minute-vaers"
cd "$REPO_DIR"

if pgrep -x git >/dev/null 2>&1; then
  echo "✗ a git process is running — close it and re-run." ; exit 1
fi
for L in .git/index.lock .git/HEAD.lock .git/config.lock .git/refs/heads/main.lock; do
  [ -f "$L" ] && rm -f "$L" && echo "→ cleared stale $L"
done

[ -f "$SRC/index.html" ] || { echo "✗ $SRC/index.html not found"; exit 1; }
mkdir -p "$DEST"
cp "$SRC/index.html" "$DEST/index.html"
cp "$SRC/README.md"  "$DEST/README.md"
cp "$SRC/the-engine-already-exists.html" "$DEST/the-engine-already-exists.html"
cp "$SRC/HISTORY_esp_vaers.md" "$DEST/HISTORY_esp_vaers.md"
echo "→ copied demo + white paper into $DEST"

git add five-minute-vaers deploy_five_minute_vaers.sh
git commit -m "Publish 5-Minute VAERS demo (v0.1) — synthetic, open, HIPAA-permitted" || echo "→ nothing new to commit"
gh auth switch --user meridian-north 2>/dev/null || true
git push origin main

echo ""
echo "✓ Done. Live (~1 min for Pages):"
echo "  https://meridian-north.github.io/vaers-1990-2026-searchable/five-minute-vaers/"
