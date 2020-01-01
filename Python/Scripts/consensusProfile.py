#!/usr/bin/python3
#Python Script to determine profile matrix of equal length sequences and a consensus sequence between them
import sys

def main(arg):
   fasta_dict = parse_fasta_dict(arg)
   a_counts,c_counts,g_counts,t_counts = pos_acgt_count(list(fasta_dict.values()))
   cons = consensus_seq(a_counts,c_counts,g_counts,t_counts)
   print("".join(cons))
   print("A:", *a_counts)
   print("C:", *c_counts)
   print("G:", *g_counts)
   print("T:", *t_counts)
   return

def consensus_seq(a_counts,c_counts,g_counts,t_counts):
   cons = []
   i = 0
   while i < len(a_counts):
      highest = 0
      if a_counts[i] > highest:
         highest = a_counts[i]
         letter = "A"
      if c_counts[i] > highest:
         highest = c_counts[i]
         letter = "C"
      if g_counts[i] > highest:
         highest = g_counts[i]
         letter = "G"
      if t_counts[i] > highest:
         highest = t_counts[i]
         letter = "T"
      cons.append(letter)
      i+=1
   return cons

def pos_acgt_count(sequences):
   a_pos = []
   c_pos = []
   g_pos = []
   t_pos = []
   i = 0
   while i < len(sequences[1]):
      a_ct = 0
      c_ct = 0
      g_ct = 0
      t_ct = 0
      for seq in sequences:
         if seq[i].upper() == "A":
            a_ct+=1
         if seq[i].upper() == "C":
            c_ct+=1
         if seq[i].upper() == "G":
            g_ct+=1
         if seq[i].upper() == "T":
            t_ct+=1
      a_pos.append(a_ct)
      c_pos.append(c_ct)
      g_pos.append(g_ct)
      t_pos.append(t_ct)
      i+=1
   return a_pos,c_pos,g_pos,t_pos

def parse_fasta_dict(filename):
   fasta_dict = {}
   strings = open(filename).read().strip().split('>')
   for line in strings:
      if len(line) == 0:
         continue
      parts = line.split()
      label = parts[0]
      bases = ''.join(parts[1:])
      fasta_dict[label] = bases
   return fasta_dict

if len(sys.argv) > 1:
   main(sys.argv[1])
else:
   print("improper usage: python3 tool.py ./filename")
