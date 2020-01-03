def trans_allORFproteins(rna):
   proteins = []
   rc_rna = RNAreverseComplement(rna)
   for seq in rna,rc_rna:
      i = 0
      while i <= 2:
         prot = str(rna2prot_frompos(seq, i))
         proteins.append(prot)
         i+=1
   return proteins
   
def RNAreverseComplement(seq):
   complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
   return "".join(complement.get(base, base) for base in reversed(seq))
