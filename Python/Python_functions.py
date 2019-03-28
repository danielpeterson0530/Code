#########################################################################
# Python Functions to use in Code.                                      #
#########################################################################

#Function to count given Pattern in a reference Text
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

#Script to calculate reverse complement of given Pattern
##Requires reverse and complement functions
def ReverseComplement(Pattern):
    reverse = Reverse(Pattern)
    reversecomplement = Complement(reverse)
    return reversecomplement

#Function to reverse a given Pattern
def Reverse(Pattern):
    return Pattern[::-1]

#Function to complement a given Pattern
def Complement(Pattern):
    Pattern = Pattern.replace("A","t")
    Pattern = Pattern.replace("T","a")
    Pattern = Pattern.replace("C","g")
    Pattern = Pattern.replace('G','c')
    Pattern = Pattern.upper()
    return(Pattern)
    # your code here

#Function to return postions of matched Pattern in Genome into Postions list
def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern)+1):
            if Pattern == Genome[i:i+len(Pattern)]:
                positions.append(i)
    return positions
