
def counts(word):
    counts = {}
    for c in word:
        if counts.get(c) == None:
            counts[c] = 1
        else:
            counts[c] +=1



    return counts
print(counts('Erdbeere'))

