'''
Basic Regex Parser
'''


def is_match(text, pattern):

    t_len = len(text)
    p_len = len(pattern)

    t = 0
    p = 0

    while p < p_len:
        if pattern[p] != "*" and pattern[p] != "." and ((p + 1 < p_len and pattern[p + 1] != "*") or (p + 1 == p_len)):
            if t < t_len and pattern[p] == text[t]:
                p += 1
                t += 1
            else:
                return False

        elif pattern[p] != "*" and pattern[p] != "." and p + 1 < p_len and pattern[p + 1] == "*":
            while t < t_len and text[t] == pattern[p]:
                t += 1
            p += 2

        elif p + 1 < p_len and pattern[p:p + 2] == ".*":
            if t < t_len:
                ch = text[t]
            while t < t_len and text[t] == ch:
                t += 1
            p += 2

        elif pattern[p] == ".":
            if t < t_len:
                t += 1
            else:
                return False
            p += 1

    return p >= p_len and t >= t_len
