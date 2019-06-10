from Common.common import *

#region Question 2.1 (remove duplicates)
def removeDups(ll: linkedList):
    n = ll.head
    dataset = set()
    prev = node()
    while n is not None:
        if n.data in dataset:
            prev.next = n.next
            # no need to change the prev pointer
        else:
            dataset.add(n.data)
            prev = n
        n = n.next

def removeDups2(ll: linkedList):
    current = ll.head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

l1 = linkedList(node(1))
l1.addLast(node(1))
l1.addLast(node(1))
l1.addLast(node(0))
l1.addLast(node(2))
l1.print()

removeDups2(l1)
l1.print()
#endregion
