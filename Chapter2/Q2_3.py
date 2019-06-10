from Common.common import *

# region Question 2.3 (delete middle node)
def deleteNode(n: node):
    if n is None or n.next is None:
        return False

    #nextNode: node = n.next
    n.data = n.next.data
    n.next = n.next.next

    return True

ll = linkedList(node(1))
ll.addLast(node(2))
ll.addLast(node(3))
ll.addLast(node(4))
ll.addLast(node(5))

ll.print()

deleteNode(ll.head.next.next)
ll.print()
deleteNode(ll.head.next)
ll.print()

# endregion
