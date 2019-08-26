'''
String One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''


def isOneAway(s: str, p: str) -> bool:
    if s == p:
        return True
    if abs(len(s) - len(p)) > 1:
        return False

    lenDiff = len(s) - len(p)
    shorter = None
    longer = None

    if lenDiff > 0:
        shorter, longer = p, s
    else:
        shorter, longer = s, p

    i = 0
    j = 0
    diff = 0

    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            diff += 1
            if lenDiff == 0:
                i += 1  # move forward only if the strings have same size, don't move shorter pointer if the string is shorter
        else:
            i += 1  # move forward if the characters are matched

        j += 1  # always move the longer pointer forward

    if diff > 1:
        return False
    return True


str1 = "Vahd"
str2 = "Vahid"

print(isOneAway(str1, str2))