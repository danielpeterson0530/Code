## Python Function to return list with set of unique ids from file column#
def get_uniq_id_list(filename, col):
   uniq_list = []
   with open(filename) as f:
      for line in f:
         elements = line.split()
         id = elements[col]
         uniq_list.append(id)
   uniq_set = set(uniq_list)
   uniq_list = (list(uniq_set))
   return uniq_list
