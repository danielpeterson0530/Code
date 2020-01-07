#!/usr/bin/bash
# Bash script to get PMC articles linked to query id
#
# Requires edirect (esearch, efetch, xtract packages) from NCBI eutils
# ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh
# API-key is suggested to avoid service denial. Otherwise set sleep to 1s.

if [ ! $# -ge 1 ]; then
        echo "usage: bash tool.sh ./file"
        exit 1
fi
IFS=$'\n'
file=$1

for id in $(cut -f4 $file); do
   if [[ -z "$id" ]]; then
      continue
   fi
   papers=$(esearch -db pmc -query "$id" | efetch -format docsum | xtract -pattern DocumentSummary -element Id Title)
   if [[ -z "$papers" ]]; then
      >&2 echo -e "$id\tnone"
   else
      for line in $papers; do
         echo -e "$id\t$line"
      done
   fi
   sleep 0.5s
done
