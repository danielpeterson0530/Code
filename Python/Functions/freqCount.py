# Python Function to return uniq list of items and freq count
def freqCount(mylist):
   freq_dict = {}
   for item in mylist:
      if item in freq_dict:
         freq_dict[item] += 1
      else:
         freq_dict[item] = 1

   for key, value in freq_dict.items():
      print(key, value)
   return
