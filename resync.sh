#!/bin/sh

# Simple utility to automate the conversion of markdown docs to a 
# standalone web site, and then push that website to github pages.
#
# Note that all directory paths are hard-coded. Sue me, it's my computer
# and it works here (okay, it's not perfect, I know - "WIBNI"...

# Rebuild html
cd ~/tvh/tvheadend-documentation
mkdocs build --clean

# Copy it to local github pages repository
cd ~/tvh/tvheadend.github.io
cp -r ~/tvh/tvheadend-documentation/site/* .

# Commit it and push
git add -A
git commit -m "Resync with source repository: `date`"
git push
