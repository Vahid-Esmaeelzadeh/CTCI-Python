# region Question 8.8 (permutations dups)
import copy

def permutationsDup(str):
    freqTable = buildFreqTable(str)
    result = permutationsDupHelper(freqTable)
    return result

def permutationsDupHelper(freqTable):
    result = []
    for i in freqTable:
        if freqTable[i] > 0:
            freqTable[i] -= 1
            lst = permutationsDupHelper(copy.deepcopy(freqTable))
            for s in lst:
                result.append(freqTable[i] + s)
    return result

def buildFreqTable(str):
    freqTable = dict()
    for c in str:
        if c not in freqTable:
            freqTable[c] = 0
        freqTable[c] += 1
    return freqTable



freqTable = buildFreqTable('baabcdd')
print(freqTable)

print(permutationsDup('ab'))
# endregion
