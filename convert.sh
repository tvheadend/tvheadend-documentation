#! /bin/sh

echo "This utility will batch convert all md files to html for use in tvheadend"
echo
echo "All existing like-named html files in the target directory will be over-written"
echo "without further prompt"

if  [ -z "$1" ] || [ -z "$2" ]; then
  echo
  echo "Insufficient number of arguments provided"
  echo
  echo "Usage: convert <sourcedir> <targetdir>"
  exit
fi

echo 
echo "** Using input directory" $1
echo "** Using output directory" $2
echo 
read -p "Press [Enter] to contine, or [Ctrl-C] to abort..." null

for inputfile in $1/*.md
do
  outputfile=$2/`basename $inputfile .md`.html
  echo "Converting "$inputfile

# File header/disclaimer
  echo "<!-- ***** WARNING! This file is auto-generated ***** -->" > $outputfile
  echo >> $outputfile
  echo "<!-- Do not edit it by hand if you want to keep your changes. -->" >> $outputfile
  echo "<!-- All changes *must* be made in the source markdown and then carried-->" >> $outputfile
  echo "<!-- through the pandoc conversion that creates these html files. -->" >> $outputfile
  echo >> $outputfile
  echo "<!-- Make changes on https://github.com/ProfYaffle/tvheadend-documentation -->" >> $outputfile
  echo >> $outputfile

# Version and date
  echo "<!-- File created on" `date` " -->" >> $outputfile
  echo "<!-- Created with" `pandoc -v | head -1` " -->" >> $outputfile
  echo >> $outputfile

# HTML - pandoc conversion inside tvheadend-specifc <div>
  echo "<div class=\"hts-doc-text\">" >> $outputfile
  pandoc $inputfile >> $outputfile
  echo "</div>" >> $outputfile

  echo "Saved as" $outputfile
  echo

done
