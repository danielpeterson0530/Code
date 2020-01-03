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
