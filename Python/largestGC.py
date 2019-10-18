#!/usr/bin/python3
import sys

def parse_fasta(file):
        parsed_fasta = {}                       #intialize empty dict
        strings = file.strip().split('>')       #remove whitespace, split on carat into list

        for line in strings:                    #for each element in list
                if len(line) == 0:              #if empty, skip
                        continue
                parts = line.split()            #split the element (newlines)
                label = parts[0]                #first split is label
                bases = ''.join(parts[1:])      #join all other elements as bases
                parsed_fasta[label] = bases     #add label and bases to dict

        return parsed_fasta


def gc_content(data):
        total_len = len(data)                   #determine length of seq
        count = 0                               #initialize count to zero

        for base in data:                       #for each base in data
                if base == 'G' or base == 'C':  #if G or C add one to count
                        count += 1

        return 100 * (float(count) / total_len) #return the number of G or C bases / total *100 (percent)


def main(arg):

        large_dataset = open(arg).read()        #load in data from argument

        parsed_fasta = parse_fasta(large_dataset)       #pass to function
                                                #build new dict with results
        results = dict([(label,gc_content(data)) for label,data in parsed_fasta.items()])

        highest_data = 0                        #initialize empty var as zero
        highest_label = None                    #same
        for label,data in results.items():      #for each entry in results
                if data > highest_data:         #test for highest GC percentage
                        highest_data = data
                        highest_label = label

        print(highest_label)                    #print highest GC% and label
        print('{:.6f}'.format(round(highest_data,6)))

        return


if len(sys.argv) > 1:                           #exit if no arguments supplied
        main(sys.argv[1])
else:
        print("improper usage: python3 tool.py ./fasta_file")
