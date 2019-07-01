def search_rotated(lst, x):
    return search_rotated_rcr(lst, x, 0, len(lst) - 1)


def search_rotated_rcr(lst, x, left, right):
    mid = (left + right) // 2

    if lst[mid] == x:
        return mid
    if right < left:
        return -1

    if lst[left] < lst[mid]:  # left side is normally ordered
        if lst[left] <= x < lst[mid]:
            return search_rotated_rcr(lst, x, left, mid - 1)
        else:
            return search_rotated_rcr(lst, x, mid + 1, right)

    elif lst[left] > lst[mid]:  # right side is normally ordered
        if lst[mid] < x <= lst[right]:
            return search_rotated_rcr(lst, x, mid + 1, right)
        else:
            return search_rotated_rcr(lst, x, left, mid - 1)

    else:  # all repeats (either left or right side)
        if lst[right] != lst[mid]:  # right side is not all repeats
            return search_rotated_rcr(lst, x, mid + 1, right)
        else:  # we have to search both sides
            result = search_rotated_rcr(lst, x, left, mid - 1)
            if result == -1:
                return search_rotated_rcr(lst, x, mid + 1, right)
            else:
                return result


a = [1, 1, 1, 20, 25, 26, 27, 28, 1, 1, 1, 1]
print(search_rotated(a, 27))