# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence


def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split()
    for i in range(len(words)):
        if words[i].startswith(searchWord):
            return i
    return -1


print(isPrefixOfWord("i love eating burger", "burg"))

