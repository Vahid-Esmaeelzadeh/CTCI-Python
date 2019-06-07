def URLify(str, n):
    lst = list(str)
    spaces = 0

    for i in range(n):
        if lst[i] == ' ':
            spaces += 1

    index = n + spaces * 2
    for i in range(n-1, -1, -1):
        if lst[i] == ' ':
            lst[index-3:index] = '%20'
            index -= 3
        else:
            lst[index-1] = lst[i]
            index -= 1

    return ''.join(lst)

print(URLify(' Vahid E    ', 8))
