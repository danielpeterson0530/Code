#Python function to count number of occurences of given pattern
def patternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count
