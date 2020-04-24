#bin/bash

##################################################################################
# Bash script that will collect full taxonomic lineage information from EBI/EMBL #
# when given a list of scientific names and return in csv format to STDOUT.      #
################################################################################## 

# NOTE: requires list of scientific names in file named 'list.of.names.txt'
## Names should be seperated by a single space, and each on their own line


echo "Scientific_name,Subphylum,Class,Order,Family"     #prints csv column info first on screen
echo

IFS=$'\n'           #tells bash to treat list.of.names.txt with newlines to create URL

while read -r line   #goes through list.of.names.txt line by line
do
	link=$(echo "https://www.ebi.ac.uk/ena/data/view/Taxon:"$line"&display=xml" | perl -pe 's/\h+/%20/g') #create URL
	IFS=     #resets to select single element in link variable
	curloutput=$(curl -s $link)   #collects XML data from online and sends to variable

	#the following greps out all of the  information from the collected XML data in curloutput
	subphylum=$(echo $curloutput | egrep "\"subphylum" | egrep -o "\".+\"" | perl -pe 's/\h+/\t/g' | cut -f1 | sed 's/\"//g')
	class=$(echo $curloutput | egrep "\"class" | egrep -o "\".+\"" | perl -pe 's/\h+/\t/g' | cut -f1 | sed 's/\"//g')
	order=$(echo $curloutput | egrep "\"order" | egrep -o "\".+\"" | perl -pe 's/\h+/\t/g' | cut -f1 | sed 's/\"//g')
	family=$(echo $curloutput | egrep "\"family" | egrep -o "\".+\"" | perl -pe 's/\h+/\t/g' | cut -f1 | sed 's/\"//g')

	#Following prints out the collecting family information in a csv style format
	echo $line","$subphylum","$class","$order","$family
done < list.of.names.txt
