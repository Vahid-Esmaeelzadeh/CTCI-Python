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
    diff = False

    while i < len(shorter):
        if shorter[i] != longer[j]:
            diff = True
            if lenDiff == 0:
                i += 1  # move forward only if the strings have same size, don't move shorter pointer if the string is shorter
        else:
            i += 1  # move forward if the characters are matched

        j += 1  # always move the longer pointer forward

        if diff:
            return False

    return True

str1 = "Vahid"
str2 = "Vahd"

print(isOneAway(str1, str2))