#!/usr/bin/python3
#converts DNA FASTA file to predicted ORF proteins in all reading frames
import sys, re

RNA_PROT_DICT = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'UAG' : '*', 'UAA' : '*', 'UGA' : '*'}

def main(arg):
   fasta_dict = fastafile2dict(arg)
   for key,value in fasta_dict.items():
      dna = value
      rna = dna2rna(dna)
      prot_trans_seqs = returnORFproteins(rna)
      orf_list = unique(regex_orfFinder(prot_trans_seqs))
      print(key)
      for orf in sorted(orf_list, key=len, reverse=True):
         print(orf)
   return

def unique(list1):
   list_set = set(list1)
   return list(list_set)

def regex_orfFinder(proteins):
## requires re package
   orf_list = []
   for prot in proteins:
      orfs = re.findall('M[^\*]*?[?=\*]', prot)
      if orfs:
         for orf in orfs:
            orf_list.append(orf.replace('*', ''))
            if orf.count("M") > 1:
               while orf.count('M') > 1:
                  repeat = '[^M\*]*[M]' * (int(orf.count('M'))-2)
                  regex = 'M'+repeat+'[^M\*]*?[?=\*]'
                  orf = re.findall(regex, orf)[0]
                  orf_list.append(orf.replace('*', ''))
   return orf_list

def returnORFproteins(rna):
   proteins = []
   rc_rna = RNAreverseComplement(rna)
   for seq in rna,rc_rna:
      i = 0
      while i <= 2:
         prot = str(rna2prot_frompos(seq, i))
         proteins.append(prot)
         i+=1
   return proteins

def rna2prot_frompos(seq, pos):
   prot_str = ""
   i = pos
   while i < len(seq):
      three_base_code = seq[i:i + 3]
      if len(three_base_code) == 3:
         if three_base_code in RNA_PROT_DICT:
            prot = RNA_PROT_DICT[three_base_code]
            prot_str = prot_str + prot
      i += 3
   return prot_str

def RNAreverseComplement(seq):
   complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
   return "".join(complement.get(base, base) for base in reversed(seq))

def dna2rna(seq):
   return seq.replace("T", "U")

def fastafile2dict(filename):
   fasta_dict = {}
   strings = open(filename).read().strip().split('>')
   for line in strings:
      if len(line) == 0:
         continue
      parts = line.split()
      label = parts[0]
      fasta_dict[label] = ''.join(parts[1:])
   return fasta_dict

if len(sys.argv) > 1:
   main(sys.argv[1])
else:
   print("improper usage: python3 tool.py ./filename")
