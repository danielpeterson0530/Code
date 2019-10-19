#Function to determine %GC content of sequence data
def gc_content(data):
        total_len = len(data)                   
        count = 0                               

        for base in data:                       
                if base == 'G' or base == 'C':  
                        count += 1

        return 100 * (float(count) / total_len) 
