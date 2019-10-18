#Function to return postions (0 indexed) of matched Pattern in Reference
def patternPositions(pattern, ref):
    positions = []
    for i in range(len(ref) - len(pattern)+1):
            if pattern == ref[i:i+len(pattern)]:
                positions.append(i)
    return positions
