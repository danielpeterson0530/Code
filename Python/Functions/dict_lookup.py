## Pythonfunction to return value from dictionary key
def dict_lookup(id, dict):
   if id in dict.keys():
      return dict[id]
   else:
      print(id, "not found in dictionary -- SKIPPING", file=sys.stderr)
      return
