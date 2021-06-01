#!/bin/bash
# Bash script to pair RNA-seq files together based on an ID within the filename, can then run a program for each pair


if [ ! $# -ge 1 ]; then
        echo "usage: bash tool.sh ./dir"
        exit 1
fi
IFS=$'\n'
dir=$1
arrVar=()

dir_regex='^.+\/'                                       #regex for dir
lead_regex='69[0-9]+_'                                  #regex for leading filename
trail_regex='_R[0-9].+$'                                #regex for trailing filename

#build array with sample ids from dir
for file in $(ls -d $dir/*); do
        filename=$(echo $file |
                sed -E 's/'$dir_regex'//g');            #regex remove dir path from filename
        sample_num=$(echo $filename |
                sed -E 's/'$lead_regex'//g' |           #regex remove leading filename before S#
                sed -E 's/'$trail_regex'//g');          #regex remove trailing filename after S#
        if [[ ! " ${arrVar[@]} " =~ " $sample_num " ]]; then
                arrVar+=("$sample_num");                #append samples to array
        fi

done

#iterate through sample ids in dir, collect file pairs
for item in "${arrVar[@]}"; do                          #iterate array
        arrPair=();
        arrPair+=($(ls -d $dir/*$item*));               #collect matching file pairs
        r1="${arrPair[0]}"                              #assign each pair
        r2="${arrPair[1]}"
        
        ####### Command to run for pair #######
        echo $r1 $r2
        #######################################
done
