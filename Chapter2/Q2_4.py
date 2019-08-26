'''
LinkedList Partition: Write code to partition a linked list around a value x, such that all Nodes less than x come
before all Nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''


from Common.common import *
import copy


# using head-pointer and other two pointers
def partition(ll: linkedList, x):
    head = ll.head

    runner = ll.head
    prev = None

    while runner is not None:
        if (runner.data < x) and (prev is not None):
            prev.next = runner.next  # remove the Node
            runner.next = head  # put the Node at the first of linked list
            head = runner

            runner = prev.next  # no need to update the prev, update the runner
        else:   # we should go forward without removing any Node
            prev = runner
            runner = runner.next

    return linkedList(head)


def partition2(n: Node, k: int):
    if n is None:
        return None

    current = n.next
    prev = n

    while current:
        if current.data < k:
            prev.next = current.next
            current.next = n
            n = current

            current = prev.next
        else:
            prev = current
            current = current.next

    return linkedList(n)


ll = linkedList(Node(3))
ll.addLast(Node(5))
ll.addLast(Node(8))
ll.addLast(Node(-10))
ll.addLast(Node(5))
ll.addLast(Node(10))
ll.addLast(Node(4))
ll.addLast(Node(2))
ll.addLast(Node(1))
ll.addLast(Node(7))

partition(copy.deepcopy(ll), -100).print()
partition(copy.deepcopy(ll), 100).print()
partition(copy.deepcopy(ll), 4).print()

l = linkedList(Node(3))
l.addLast(Node(5))
l.addLast(Node(8))
l.addLast(Node(-10))
l.addLast(Node(5))
l.addLast(Node(10))
l.addLast(Node(4))
l.addLast(Node(2))
l.addLast(Node(1))
l.addLast(Node(7))


partition2(l.head, 100).print()

