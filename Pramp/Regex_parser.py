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

        elif pattern[p] == "*":  # ".*"
            ch = ""
            if t < t_len:
                ch = text[t]
                t += 1
            while t < t_len and text[t] == ch:
                t += 1
            p += 1

        elif pattern[p] == ".":
            if t < t_len:
                t += 1
            else:
                return False
            p += 1

    return p >= p_len and t >= t_len


def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


# my solution - basic recursive
def isMatch1(text, pattern):
    return helper(text, pattern, 0, 0)


def helper(text, pattern, i, j):
    # if j == len(pattern):
    #     return i == len(text)

    if j == len(pattern) and i == len(text):
        return True
    if j == len(pattern) and i < len(text):
        return False

    first_match = i < len(text) and pattern[j] in {text[i], '.'}

    if j + 1 < len(pattern) and pattern[j + 1] == '*':
        return (helper(text, pattern, i, j + 2) or
                first_match and helper(text, pattern, i + 1, j))
    else:
        return first_match and helper(text, pattern, i + 1, j + 1)


# memoization
def isMatch_memo(text, pattern):
    memo = [[None for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)]
    res = helper_memo(text, pattern, 0, 0, memo)
    print(memo)
    return res


def helper_memo(text, pattern, i, j, memo):
    if j == len(pattern):
        return i == len(text)

    if memo[i][j] is not None:
        return memo[i][j]

    # if j == len(pattern) and i == len(text):
    #     return True
    # if j == len(pattern) and i < len(text):
    #     return False

    first_match = i < len(text) and pattern[j] in {text[i], '.'}

    if j + 1 < len(pattern) and pattern[j + 1] == '*':
        memo[i][j] = helper_memo(text, pattern, i, j + 2, memo) or \
                     (first_match and helper_memo(text, pattern, i + 1, j, memo))
        return memo[i][j]
    else:
        memo[i][j] = first_match and helper_memo(text, pattern, i + 1, j + 1, memo)
        return memo[i][j]


# tabulation
def is_match_tabulation(text, pattern):
    t_len = len(text)
    p_len = len(pattern)
    dp = [[False for _ in range(p_len + 1)] for _ in range(t_len + 1)]

    dp[t_len][p_len] = True

    for i in range(t_len, -1, -1):
        for j in range(p_len-1, -1, -1):
            first_match = i < t_len and pattern[j] in {text[i], '.'}
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
            else:
                dp[i][j] = first_match and dp[i + 1][j + 1]
    print(dp)
    return dp[0][0]


def is_match_tabulation_opt(text, pattern):
    t_len = len(text)
    p_len = len(pattern)
    dp = [[False for _ in range(p_len + 1)] for _ in range(2)]

    for i in range(t_len, -1, -1):
        if i == t_len:
            dp[i % 2][p_len] = True
        else:
            dp[i % 2][p_len] = False
        for j in range(p_len - 1, -1, -1):
            first_match = i < t_len and pattern[j] in {text[i], '.'}
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                dp[i % 2][j] = dp[i % 2][j + 2] or (first_match and dp[(i + 1) % 2][j])
            else:
                dp[i % 2][j] = first_match and dp[(i + 1) % 2][j + 1]
    return dp[0][0]


text = "abbbzdf"
pattern = ".b*.*f"
print(is_match_tabulation_opt(text, pattern))

