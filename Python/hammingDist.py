#!/usr/bin/python3
import sys
def main(arg):

        large_dataset = open(arg).read().split()
        seq_1 = str(large_dataset[0])
        seq_2 = str(large_dataset[1])
        h_dist = 0
        i = 0
        while i < len(seq_1):
                if seq_1[i] != seq_2[i]:
                        h_dist += 1
                i += 1
        print(h_dist)
        return


if len(sys.argv) > 1:
        main(sys.argv[1])
else:
        print("improper usage: python3 tool.py ./file")
