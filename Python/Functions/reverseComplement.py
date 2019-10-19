#Function to calculate reverse complement of given Pattern
##Requires reverse and complement functions

def reverseComplement(pattern):
    reverse = reverse(pattern)
    reversecomplement = complement(reverse)
    return reversecomplement

#Function to reverse a given Pattern
def reverse(pattern):
    return pattern[::-1]

#Function to complement a given Pattern
def complement(pattern):
    pattern = pattern.replace("A","t")
    pattern = pattern.replace("T","a")
    pattern = pattern.replace("C","g")
    pattern = pattern.replace('G','c')
    pattern = pattern.upper()
    return(pattern)
