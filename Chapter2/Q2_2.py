'''
Return Kth to Last: Implement an algorithm to fnd the kth to last element of a singly linked list.
'''

from Common.common import *


# size-based solution
def kLast_basic(lst:linkedList, k:int):
    _size = lst.size()
    i = _size - k

    current = lst.head
    while (current is not None) and i > 0:
        current = current.next
        i -= 1

    return current


# recursive
def kLast_recr(ll:linkedList, k:int):
    kLast_helper(ll.head, k)


# two-pointer solution
def kLast_helper(n: Node, k: int):
    if n is None:
        return 0
    index = kLast_helper(n.next, k) + 1
    if index == k:
        print(k, "th to the last node is ", n.data)
    return index


def kLast(ll: linkedList, k:int):
    if k <= 0:
        return None

    current = ll.head
    runner = ll.head
    i = 0

    while i < k:
        if runner is None:
            return None
        runner = runner.next
        i += 1

    while runner:
        current = current.next
        runner = runner.next

    return current.data


ll = linkedList(Node(1))
ll.addLast(Node(2))
ll.addLast(Node(3))
ll.addLast(Node(4))
ll.addLast(Node(5))

item = kLast_basic(ll, -1)
kLast_recr(ll, 1)
print(kLast(ll, 0))

