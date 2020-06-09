# 1451. Rearrange Words in a Sentence
import math


def arrangeWords(text: str) -> str:
    count_word_map = {}
    words = text.split()
    for word in words:
        if len(word) in count_word_map:
            count_word_map[len(word)].append(word.lower())
        else:
            count_word_map[len(word)] = [word.lower()]

    sorted_hash_map = sorted(count_word_map.items(), key=lambda kv: kv[0])

    result = []
    for count, words in sorted_hash_map:
        for word in words:
            result.append(word)

    if len(result) > 0:
        first_word = result[0]
        result[0] = first_word[0].upper() + first_word[1:]

    return ' '.join(result)


def arrangeWords1(text: str) -> str:
    count_word_map = {}
    words = text.split()
    min_len, max_len = math.inf, -math.inf
    for word in words:
        if len(word) in count_word_map:
            count_word_map[len(word)].append(word.lower())
        else:
            count_word_map[len(word)] = [word.lower()]

        min_len = min(min_len, len(word))
        max_len = max(max_len, len(word))

    result = []

    for length in range(min_len, max_len + 1):
        if length in count_word_map:
            for word in count_word_map[length]:
                result.append(word)

    if len(result) > 0:
        first_word = result[0]
        result[0] = first_word[0].upper() + first_word[1:]

    return ' '.join(result)


def arrangeWords2(text: str) -> str:
    return " ".join(sorted(text.split(" "), key=len)).capitalize()


print(arrangeWords("Interviewboost is COOL"))
print(arrangeWords1("Interviewboost is COOL"))
print(arrangeWords2("Interviewboost is COOL"))
