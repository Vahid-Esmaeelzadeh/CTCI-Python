'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE
lnput:the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a ->b->d->e->f
'''

from Common.common import *


def deleteNode(n: Node):
    if n is None or n.next is None:
        return False

    n.data = n.next.data
    n.next = n.next.next

    return True

ll = linkedList(Node(1))
ll.addLast(Node(2))
ll.addLast(Node(3))
ll.addLast(Node(4))
ll.addLast(Node(5))

ll.print()

deleteNode(ll.head.next.next)
ll.print()
deleteNode(ll.head.next.next)
ll.print()

