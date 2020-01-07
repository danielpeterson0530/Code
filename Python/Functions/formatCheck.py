## Python Function that checks filename for equal to or greater than number of columns supplied and exits with error message if not true (requires csv)
def format_check(filename, num_cols):
### Requires csv package
   with open(filename) as f:
      reader = csv.reader(f, delimiter='\t', skipinitialspace=True)
      first_row = next(reader)
      cols = len(first_row)
      if not cols >= num_cols:
         print("file: \"",filename,"\" not correct format. Requires (", num_cols, ") or more columns.", file=sys.stderr)
         sys.exit(0)
   return
