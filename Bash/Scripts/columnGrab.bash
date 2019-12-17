#!/usr/bin/bash
#Returns columns based on user entry from gzip file. 

if [ ! $# -ge 2 ]; then
        echo "usage: bash tool.sh TAXID ./gene2*.gz"
        exit 1
fi

IFS=$'\n'
taxid=$1
g2a=$2

first_line=$(less $g2a | head -n 1)
num_col=$(echo $first_line | awk '{print NF}')

i=1
while [ $i -le $num_col ];
do
        col=$(echo $first_line | cut -f $i)
        echo -e "COL"$i"\t"$col
        i=$[$i+1]
done

echo "-----"
echo "Which column contains the taxid?"
read sort_col
if [[ ! $sort_col =~ [0-9] ]];then
        echo "unknown entry: "$sort_col
        exit 1
fi
echo "which columns do you wish to keep? (seperate with commas ie: 1,2,3)"
read column_keep
if [[ ! $column_keep =~ [0-9\,]+ ]];then
        echo "unknown entry: "$column_keep
        exit 1
fi
echo "running ..."

outfile="$taxid""_entries.txt"
if [ ! -e $outfile ];then
        awk_col="$sort_col"
        zgrep -w "$taxid" $g2a | awk -v taxid="$taxid" -v column="$awk_col" '{if ( $column == taxid ) print $0}' | cut -f $column_keep > "$outfile"
fi
count=$(less "$outfile" | wc -l)
echo
echo $count" entries found. Done."
