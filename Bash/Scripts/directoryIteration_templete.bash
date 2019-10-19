#!/usr/bin/bash
#Lightweight templete for iterating through a directory and running operations on every file
if [ ! $# -ge 2 ];then
        echo "usage: tool.sh ./dir-of-files OUTPUT_EXT"
        exit 1
fi

files=$(ls -d $1/*)
output_name=$2

for file in $files
do
##### Command line operations to complete for each "$file" ########


##################################################################
done
