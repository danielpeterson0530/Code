#Function to parse large fasta files into dictionary with label and sequence
def parse_fasta(file):
        parsed_fasta = {}                       
        strings = file.strip().split('>')       

        for line in strings:                   
                if len(line) == 0:           
                        continue
                parts = line.split()          
                label = parts[0]              
                bases = ''.join(parts[1:])    
                parsed_fasta[label] = bases     

        return parsed_fasta
