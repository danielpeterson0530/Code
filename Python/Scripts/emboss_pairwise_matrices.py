#!/usr/bin/python3
# Python Script to run local EMBOSS Needle/Water Pairwise Alignment iteratively and print Matrices for Percent Identitiy and Percent Similarity
import sys, subprocess, re

def main(filename, test_choice, table_choice):
   test_name = check_input(test_choice, table_choice)
   fasta_list = fastafile2list(filename)
   max_slen = len(max([ item[0].split()[0] for item in fasta_list ], key = len)) + 4
   full_fasta = open(filename).read()
   allpids = []
   allpsims = []

   print("running", file=sys.stderr, end="") ###progress bar, prints to stderr
   i = 0
   while i < len(fasta_list):
      first_fasta = str(">" + "\n".join(fasta_list[i]))
      print(".", file=sys.stderr, end="", flush=True)
      cmd = " ".join((str(test_choice), str("<(echo -e \"" + str(first_fasta) + "\")"), str("<(echo -e \"" + str(full_fasta) + "\")"), "-auto", "-stdout"))

      output = run_cmd(cmd)
      pids = parse_output(output, "Identity")
      psims = parse_output(output, "Similarity")
      allpids.append(list(pids))
      allpsims.append(list(psims))
      i+=1
   print("done.\n", file=sys.stderr, flush=True) ###end progress bar

### PID PRINT ###
   if str(table_choice) == 'b' or str(table_choice) == 'p':
      print("\n#\n#")
      print("#", test_name, "- Percent Identity Matrix", end = '\t', flush=True)
      print("\n# ( Custom Script by Daniel Peterson )\n#\n")
      i = 0
      while i < len(allpids):
         printline = []
         for entry in allpids:
            printline.append(entry[i])
         format_var = "".join( ('{:>7s}', '{:', str(max_slen ) , 's}', '{:7s}'*len(allpids) ))
         print(format_var.format( str(str(i+1) + ": "), str(fasta_list[i][0].split()[0]), *printline) )
         i+=1
      print()

### %SIM PRINT ###
   if str(table_choice) == 'b' or str(table_choice) == 's':
      print("\n#\n#")
      print("#", test_name, "- Percent Similarity Matrix", end = '\t', flush=True)
      print("\n# ( Custom Script by Daniel Peterson )\n#\n")
      i = 0
      while i < len(allpsims):
         printline = []
         for entry in allpsims:
            printline.append(entry[i])
         format_var = "".join( ('{:>7s}', '{:', str(max_slen ) , 's}', '{:7s}'*len(allpsims) ))
         print(format_var.format( str(str(i+1) + ": "), str(fasta_list[i][0].split()[0]), *printline) )
         i+=1

   return

def parse_output(output, item):
   items = []
   for line in output.split("\n"):
      hit = re.search(item, line)
      if hit:
         percent = re.findall('[\d.]+%', line)[0]
         items.append(percent.rstrip("%"))
   return items

def run_cmd(cmd):
   p = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
   (output, err) = p.communicate()
   p_status = p.wait()
   return output.decode('utf-8').strip()

def is_tool(tool_name):
   from shutil import which

   if which(tool_name) is None:
      print("Cannot execute EMBOSS needle/water. Is it installed?, file=sys.stderr")
      exit(1)
   return

def check_input(test_choice, table_choice):
   if str(test_choice) == "needle" or str(test_choice) == "water":
      is_tool(str(test_choice))
   else:
      print("bad test choice: (", str(test_choice), "): improper usage: python3 tool.py ./fasta_filename (needle|water) [%PID(p)|%SIM(s)|Both(b) default]", file=sys.stderr)
      exit(1)

   if not str(table_choice) in ("b", "p", "s"):
      print("bad table choice (", str(table_choice), "): improper usage: python3 tool.py ./fasta_filename (needle|water) [%PID(p)|%SIM(s)|Both(b) default]", file=sys.stderr)
      exit(1)

   if str(test_choice) == "needle":
      test_name = "EMBOSS Needle Needleman-Wunsch Global Alignment"
   elif str(test_choice) == "water":
      test_name = "EMBOSS Water Smith-Waterman Local Alignment"

   return test_name

def fastafile2list(filename):
   fasta_list = []
   strings = open(filename).read().strip().split('>')
   for line in strings:
      if len(line) == 0:
         continue
      parts = line.split('\n')
      label = parts[0]
      fasta_list.append((label, ''.join(parts[1:])))
   return fasta_list


if len(sys.argv) == 4:
   main(sys.argv[1], sys.argv[2], sys.argv[3])
elif len(sys.argv) == 3:
   main(sys.argv[1], sys.argv[2], "b")
else:
   print("improper usage: python3 tool.py ./fasta_filename (needle|water) [%PID(p)|%SIM(s)|Both(b) default]")
