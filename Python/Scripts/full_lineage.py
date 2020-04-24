#!/usr/bin/python3
#Python Script to determine full tax lineage starting from taxid
import sys, subprocess

def main(arg1, arg2):
   taxid = arg1
   choice = arg2
   link = "".join(["\"https://www.ebi.ac.uk/ena/data/view/Taxon:",str(taxid),"&display=xml\""])
   cmd = " ".join(["curl -s", str(link), "&& sleep 1s"])
   xml = run_cmd(cmd)
   if "not" and "found." in xml.split():
      print("Error: taxid (", taxid, ") not recognized", file=sys.stderr)
      exit(1)
   if choice == "t":
      print_taxid_lineage(xml)
   elif choice == "n":
      print_names_lineage(xml)
   return

def print_taxid_lineage(xml):
   ids = []
   taxid_id = xml.split("\n")[2].split("\"")[3]
   ids.insert(0, taxid_id)
   lines = xml.split("lineage")[1].split("\n")
   for line in lines:
      elements = line.split("\"")
      if not len(elements) > 2:
         continue
      if elements[2] == ' taxId=':
         ids.insert(0, elements[3])

   print(",".join(ids))
   return

def print_names_lineage(xml):
   names = []
   taxid_name = xml.split("\n")[2].split("\"")[1]
   names.insert(0, taxid_name)
   lines = xml.split("lineage")[1].split("\n")
   for line in lines:
      elements = line.split("\"")
      if not len(elements) > 2:
         continue
      if elements[2] == ' taxId=':
         names.insert(0, elements[1])

   print(",".join(names))
   return

def run_cmd(cmd):
   p = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
   (output, err) = p.communicate()
   p_status = p.wait()
   return output.decode('utf-8').strip()

if len(sys.argv) == 2:
   main(sys.argv[1], "n")
elif len(sys.argv) == 3:
   main(sys.argv[1], sys.argv[2])
else:
   print("improper usage: python3 tool.py taxid [names(n)*default|taxids(t)]")
