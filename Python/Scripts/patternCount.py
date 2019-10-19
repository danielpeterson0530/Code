#!/usr/bin/python3
import sys

def patternCount(pattern, dna):
        positions = []
        for i in range(len(dna) - len(pattern)+1):
                if pattern == dna[i:i+len(pattern)]:
                        positions.append(i+1)
        print(*positions, sep = ' ')
        return


def main(arg):
        data = open(arg).read().split()
        dna = str(data[0])
        pattern = str(data[1])
        patternCount(pattern, dna)
        return

if len(sys.argv) > 1:
        main(sys.argv[1])
else:
        print("improper usage: python3 tool.py ./file")
