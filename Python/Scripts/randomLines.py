#!/usr/bin/python3
# Python script to select n number of random lines from a file and print them (requires sys, random packages)
import sys, random

def main(arg1, arg2):
   id_list = get_id_list(arg1)
   sample_list = random.sample(id_list, k=int(arg2))
   for line in sample_list:
      print(line.strip())
   return

def get_id_list(filename):
   id_list = []
   with open(filename) as f:
      for line in f:
         id_list.append(line)
   return id_list

if len(sys.argv) > 2:
   main(sys.argv[1], sys.argv[2])
else:
   print("improper usage: python3 tool.py ./filename n")
