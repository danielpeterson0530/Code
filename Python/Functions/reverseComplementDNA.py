#Python function to return reverse complement of DNA
def DNAreverseComplement(seq):
   complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
   return "".join(complement.get(base, base) for base in reversed(seq))
