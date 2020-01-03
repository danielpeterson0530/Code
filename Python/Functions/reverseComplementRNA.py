#Python function to return reverse complement of RNA
def RNAreverseComplement(seq):
   complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
   return "".join(complement.get(base, base) for base in reversed(seq))
