#!/usr/bin/bash
# Bash script to get Accession.version, organism name, GI#, and common name
# for each matched subject (accession.version) in multiple blast outfmt6 results files.
#
# Requires edirect (esearch, efetch, xtract packages) from NCBI eutils
# ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh
# API-key is suggested to avoid service denial. Otherwise set sleep to 1s.

if [ ! $# -ge 1 ]; then
        echo "usage: bash tool.sh ./dir"
        exit 1
fi
IFS=$'\n'
dir=$1

for file in $(ls -d $dir/*); do
   for id in $(cut -f2 $file); do
      id=$(echo $id | egrep -o '[A-Z0-9_]+\.[0-9]');
      esearch -db protein -query "$id" | \
      efetch -format gpc | \
      xtract -pattern INSDSeq \
      -element INSDSeq_accession-version INSDSeq_organism \
      -last INSDSeqid \
      -block INSDQualifier -if INSDQualifier_name -equals 'locus_tag' -element INSDQualifier_value;

      sleep 0.5s
   done
done
