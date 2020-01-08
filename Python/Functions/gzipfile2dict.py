# Python Function to gunzip file and return dictionary (requires gzip package)
def gzipfile2dict(filename):
# requires gzip package
   gzip_dict = {}
   with gzip.open(filename, mode='rt') as f:
      for line in f:
         elements = line.strip().split('\t')
         label = elements[0]
         id = elements[4]
         gzip_dict[label] = str(gzip_dict.get(label, "")) + str(id) + "\t"
   return gzip_dict
