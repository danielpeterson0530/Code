#!/usr/bin/bash
# Bash script to extract original fasta sequence from a large fasta file given a list of ids
if [ ! $# -ge 2 ]; then
        echo "incorrect arguments. Usage: bash tool.bash ./list_of_genes ./.faa_database_to_search_in"
        exit 1
fi

infile="$1"
original_fasta_file="$2"

while read line; do
   if grep -qw $line "$original_fasta_file"; then
      echo $line
      grep -A 10000 -w $line "$original_fasta_file" | sed -n -e '1,/>/ {/>/ !{'p''}}
   else
      1>&2 echo "$line -- ERROR sequence not found."
   fi
done < "$infile"
