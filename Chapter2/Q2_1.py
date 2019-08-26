'''
LinkedList Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buﬀer is not allowed?
'''

from Common.common import *


# using Hash-Set
def removeDups(ll: linkedList):
    n = ll.head
    dataset = set()
    prev = Node()
    while n:
        if n.data in dataset:
            prev.next = n.next
            # no need to change the prev pointer
        else:
            dataset.add(n.data)
            prev = n
        n = n.next


# using two-pointers (current/runner method)
def removeDups2(ll: linkedList):
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


l1 = linkedList(Node(1))
l1.addLast(Node(1))
l1.addLast(Node(1))
l1.addLast(Node(0))
l1.addLast(Node(2))
l1.print()

removeDups2(l1)
l1.print()
