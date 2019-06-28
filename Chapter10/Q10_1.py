def merge_b2a(a, b, size_a):
    ia = size_a - 1
    ib = len(b) - 1
    im = size_a + len(b) - 1

    while ib >= 0:
        if ia >= 0 and b[ib] < a[ia]:
            a[im] = a[ia]
            ia -= 1
        else:
            a[im] = b[ib]
            ib -= 1
        im -= 1

lst1 = [1, 20, 30, 60, None, None, None, None, None, None, None]
lst2 = [-1, 10, 15, 56, 78, 80]

merge_b2a(lst1, lst2, 4)
print(lst1)