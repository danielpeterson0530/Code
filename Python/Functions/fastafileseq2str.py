def fastafileseq2str(filename):
   strings = open(filename).read().strip().split('>')
   for line in strings:
      if len(line) == 0:
         continue
      parts = line.split()
      label = parts[0]
      bases_str = ''.join(parts[1:])
   return bases_str
