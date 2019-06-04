#region Question 2.1
from LinkedList import *

def removeDups(ll:LinkedList):
    cur = ll.head
    buffer = []
    prev = None
    while cur:
        if cur.data in buffer:
            prev.next = cur.next
            cur = prev.next
        else:
            buffer.append(cur.data)
            prev = cur
            cur = cur.next

list1 = LinkedList()
n1 = llNode('x')
n2 = llNode(2)
n3 = llNode(1)
n4 = llNode('x')
n5 = llNode(7)

list1.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

list1.printlist()
removeDups(list1)
list1.printlist()

#endregion
