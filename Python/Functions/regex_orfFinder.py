def regex_orfFinder(proteins):
## requires re package
   orf_list = []
   for prot in proteins:
      orfs = re.findall('M[^\*]*?[?=\*]', prot)
      if orfs:
         for orf in orfs:
            orf_list.append(orf.replace('*', ''))
            if orf.count("M") > 1:
               while orf.count('M') > 1:
                  repeat = '[^M\*]*[M]' * (int(orf.count('M'))-2)
                  regex = 'M'+repeat+'[^M\*]*?[?=\*]'
                  orf = re.findall(regex, orf)[0]
                  orf_list.append(orf.replace('*', ''))
   return orf_list
