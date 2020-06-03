#python3 function to make dictionary using 1st column as key
def file2dict(filename):
   file_dict = {}
   with open(filename) as f:
      for line in f:
         if len(line) == 0:
            continue
         parts = line.split()
         label = parts[0]
         file_dict[label] = "\t".join(parts[1:])
   return fasta_dict
