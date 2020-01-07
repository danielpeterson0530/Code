## Python function to build dictionary with key as column 1 entry and values as column 2 entry from file
def file_to_dict(filename):
   dict = {}
   with open(filename) as f:
      for line in f:
         values = line.split("\t")
         dict[values[0]] = values[1].strip()
   return dict
