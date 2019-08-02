from collections import deque


def case_permutations(in_str: str):
    result = deque()
    result.append("")

    for i in range(len(in_str)):
        temp_len = len(result)
        for _ in range(temp_len):
            s = result.popleft()
            if in_str[i].isdigit():
                result.append(s + in_str[i])
            elif in_str[i].islower() or in_str.isupper():
                result.append(s + in_str[i].lower())
                result.append(s + in_str[i].upper())

    return list(result)


def case_permutations2(in_str: str):
    result = []
    result.append(in_str)

    for i in range(len(in_str)):
        if in_str[i].isalpha():
            n = len(result)
            for j in range(n):
                characters = list(result[j])
                characters[i] = characters[i].swapcase()
                result.append(''.join(characters))

    return result


print(case_permutations("ab52c"))
print(case_permutations2("ab52c"))


