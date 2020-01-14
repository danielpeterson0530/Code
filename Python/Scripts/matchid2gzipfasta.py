#!/usr/bin/python3
# Python script to match a list of fasta ids (w/o >) to master gzip fasta sequence file
import sys,gzip


def main(arg1, arg2):
   fasta_dict = fastafile2dict(arg2)
   for line in open(arg1).read().strip().split('\n'):
      if line in fasta_dict.keys():
         print('>' + line)
         print(fasta_dict[line])
      else:
         print("file: ",line," not found.", file=sys.stderr)
   return


def fastafile2dict(filename):
   fasta_dict = {}
   for line in gzip.open(filename, mode='rt').read().strip().split('>'):
      if len(line) == 0:
         continue
      parts = line.split()
      label = str(parts[0])
      fasta_dict[label] = ''.join(parts[1:])
   return fasta_dict

## requires sys package
if len(sys.argv) > 2:
   main(sys.argv[1], sys.argv[2])
else:
   print("improper usage: python3 tool.py ./id_file ./fasta_file.gzip")
