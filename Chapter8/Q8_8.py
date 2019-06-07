# region Question 8.8 (permutations dups)

def permutationsDup(str):
    freqTable = buildFreqTable(str)
    result = permutaionsDupHelper(freqTable)
    return result


def permutaionsDupHelper(freqTable):
    result = []
    for i in freqTable.keys():
        if freqTable[i] > 0:
            freqTable[i] = freqTable[i] - 1
            lst = permutaionsDupHelper(freqTable)
            for s in lst:
                result.append(freqTable[i] + s)
    return result

def buildFreqTable(str):
    freqTable = dict()
    for c in str:
        if c not in freqTable:
            freqTable[c] = 0;
        freqTable[c] = freqTable[c] + 1
    return freqTable



freqTable = buildFreqTable('baabcdd')
print(freqTable)

print(permutationsDup('abbccc'))
# endregion
