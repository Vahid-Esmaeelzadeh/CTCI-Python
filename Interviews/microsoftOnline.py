# I will write my answers in Python, as I talked to recruiter.

# I have to check if the N is even or odd:
# if N is even:
    # I can start form -N/2 to N/2 ignoring 0

# if N is odd
    # I can start form -N/2 to N/2

def solution(N):
    if N % 2 == 1:
        return list(range(-N//2 + 1, N//2 + 1))
    else:
        return list(range(-N//2, 0)) + list(range(1, N//2 + 1))

print(solution(6))


def solution1(st):
    if len(st) == 0:
        return 0

    hashMap = {}
    maxCount = 0

    # Calculate and save the frequency of each character in hashMap
    for char in st:
        hashMap[char] = hashMap.get(char, 0) + 1
        maxCount = max(maxCount, hashMap[char])

    charFreq = hashMap.values()
    maximumPossibleFreq = list(range(max(charFreq), max(charFreq) - len(charFreq), -1))

    charFreq = sorted(charFreq, reverse=True)

    ans = 0
    for i in range(len(charFreq)):
        temp = max(charFreq[i] - max(maximumPossibleFreq[i], 0), 0)
        ans += temp

    return ans


print(solution1("vahidesmaeelzadeh"))



