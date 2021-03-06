'''
String Permutations by changing case

Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:
Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"

'''


def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)
    # process every character of the string one by one
    for i in range(len(str)):
        if str[i].isalpha():  # only process characters, skip digits
            # we will take all existing permutations and change the letter case appropriately
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])  # we have to use list(.) because string is immutable and we need changing
                # if the current character is in upper case, change it to lower case or vice versa
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations


def casePermutation(st):
    return helper(st, 0)


def helper(st, i):
    if i >= len(st):
        return [""]

    result = []
    rest = helper(st, i + 1)

    if st[i].isalpha():
        for x in rest:
            result.append(st[i].lower() + x)
            result.append(st[i].upper() + x)
    else:
        for x in rest:
            result.append(st[i] + x)

    return result


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))
    print(casePermutation("ab7c"))

main()
