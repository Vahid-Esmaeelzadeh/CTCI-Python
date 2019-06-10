
from Common.common import *
import copy

# region Question 2.4 (Partition)
def partition(ll: linkedList, x):
    head = ll.head

    runner = ll.head
    prev = None

    while runner is not None:
        if (runner.data < x) and (prev is not None):
            prev.next = runner.next  # remove the node
            runner.next = head  # put the node at the first of linked list
            head = runner

            runner = prev.next  # no need to update the prev, update the runner
        else:   # we should go forward without removing any node
            prev = runner
            runner = runner.next

    return linkedList(head)


def partition2(n: node, k: int):
    if n is None:
        return None

    current = n.next
    prev = n

    while current is not None:
        if current.data < k:
            prev.next = current.next
            current.next = n
            n = current

            current = prev.next
        else:
            prev = current
            current = current.next

    return linkedList(n)


ll = linkedList(node(3))
ll.addLast(node(5))
ll.addLast(node(8))
ll.addLast(node(-10))
ll.addLast(node(5))
ll.addLast(node(10))
ll.addLast(node(4))
ll.addLast(node(2))
ll.addLast(node(1))
ll.addLast(node(7))

partition(copy.deepcopy(ll), -100).print()
partition(copy.deepcopy(ll), 100).print()
partition(copy.deepcopy(ll), 4).print()

l = linkedList(node(3))
l.addLast(node(5))
l.addLast(node(8))
l.addLast(node(-10))
l.addLast(node(5))
l.addLast(node(10))
l.addLast(node(4))
l.addLast(node(2))
l.addLast(node(1))
l.addLast(node(7))


partition2(l.head, 100).print()
# endregion
