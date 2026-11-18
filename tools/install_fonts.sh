#!/usr/bin/env bash
# Installs DM Sans, the font of the PG master template, for LibreOffice renders.
# Without it LibreOffice substitutes another font and the pages fall differently from Word.
set -euo pipefail
dest="${HOME}/.local/share/fonts"
mkdir -p "$dest"
css=$(curl -fsS -A "Mozilla/4.0" "https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400;1,700")
echo "$css" | python3 -c '
import re,sys,subprocess
css=sys.stdin.read(); dest=sys.argv[1]
for st,w,u in re.findall(r"font-style: (\w+);\s*font-weight: (\d+);\s*src: url\(([^)]+)\)",css):
    fn="%s/DMSans-%s%s.ttf"%(dest,w,"i" if st=="italic" else "")
    subprocess.run(["curl","-fsS","-o",fn,u],check=True); print(fn)
' "$dest"
fc-cache -f >/dev/null
fc-match "DM Sans"
