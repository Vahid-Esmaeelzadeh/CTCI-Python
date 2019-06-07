from Common.common import *
import copy

# region Question 2.4 (Partition)
def partition(ll: linkedList, x):
    head = ll.head

    runner = ll.head
    prev = None

    while runner is not None:
        if (runner.data < x) and (prev is not None):
            n = runner
            prev.next = n.next  # remove the node
            n.next = head  # put the node at the first of linked list
            head = n

            runner = prev.next  # no need to update the prev, update the runner
        else:   # we should go forward without removing any node
            prev = runner
            runner = runner.next

    return linkedList(head)

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

# endregion
