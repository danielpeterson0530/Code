def rna2prot_frompos(seq, pos):
   prot_str = ""
   i = pos
   while i < len(seq):
      three_base_code = seq[i:i + 3]
      if len(three_base_code) == 3:
         if three_base_code in RNA_PROT_DICT:
            prot = RNA_PROT_DICT[three_base_code]
            prot_str = prot_str + prot
      i += 3
   return prot_str
