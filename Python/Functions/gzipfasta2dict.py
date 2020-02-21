#python function to open gzip fasta and return dictionary
#requires gzip package
def gzipfasta2dict(filename):
   gzip_dict = {}
   for line in gzip.open(filename, mode='rt').read().strip().split(">"):
      if len(line) == 0:
         continue
      parts = line.split()
      all_label = parts[0]
      label = all_label.split("|")[-1]
      gzip_dict[label] = ''.join(parts[1:])
   return gzip_dict
