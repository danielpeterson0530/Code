#!/usr/bin/python3
import sys

min_query_coverage = 0.7

def main(arg):
        data = open(arg).read().strip().split("\n")
        for line in data:
                elements = line.split("\t")
                qend = int(elements[7])
                qstart = int(elements[6])
                length = int(elements[3])
                query_coverage = ((qend - (qstart +1)) / length)
                if query_coverage > min_query_coverage:
                        print(line,"\t",round(query_coverage,3))
        return


if len(sys.argv) > 1:
        main(sys.argv[1])
else:
        print("improper usage: python3 tool.py ./file")
