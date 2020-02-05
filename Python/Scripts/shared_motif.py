#!/usr/bin/python3
#Python Script to determine the oongest shared motif between the sequences in a fasta file
import sys

def main(arg1):
   seqs = fastafileseqs2array(arg1)

   longest_seq_store = ""
   for i in range(len(seqs)-1):
      if longest_seq_store == "":
         longest_seq_store = shared_string(seqs[i], seqs[i+1])
      else:
         new_seq = shared_string(seqs[i+1], longest_seq_store)
         if len(longest_seq_store) >= len(new_seq):
            longest_seq_store = new_seq

   print(longest_seq_store)
   return

def shared_string(seq1, seq2):
#function to determine the longest consensus sequence between two sequences
   if len(seq2) > len(seq1):
      seq1, seq2 = seq2, seq1
   seq_length = len(seq2)
   for position in range(seq_length):
       for next_position in range(position + 1):
           common_seq = seq2[next_position: seq_length - position + next_position]
           if common_seq in seq1:
               return common_seq

def fastafileseqs2array(filename):
#function to load fasta sequences and return them in an array
   seqs = []
   strings = open(filename).read().strip().split('>')
   for line in strings:
      if len(line) == 0:
         continue
      parts = line.split()
      label = parts[0]
      seqs.append(''.join(parts[1:]))
   return seqs

## requires sys package
if len(sys.argv) > 1:
   main(sys.argv[1])
else:
   print("improper usage: python3 tool.py ./fasta_filename")
