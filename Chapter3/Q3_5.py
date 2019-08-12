'''

Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

'''


def sortStack(s1: list):
    s2 = []

    while len(s1) > 0:
        tmp = s1.pop()
        while len(s2) > 0 and s2[-1] > tmp:
            s1.append(s2.pop())
        s2.append(tmp)

    while len(s2) > 0:
        s1.append(s2.pop())


list1 = [10, -100, 3, 1.55, 7, -1, 2, 1]
sortStack(list1)
print(list1)

