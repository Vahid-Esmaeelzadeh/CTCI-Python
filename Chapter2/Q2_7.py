'''
LinkedList Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
'''


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class tailAndSize:
    def __init__(self, tail: node, n: int):
        self.size = n
        self.tail = tail

def findIntersection(list1: node, list2: node):
    if (list1 is None) or (list2 is None):
        return None

    # get tails and sizes
    tailAndSize1 = getTailAndSize(list1)
    tailAndSize2 = getTailAndSize(list2)

    # If different tails -> we don't have  any intersection
    if tailAndSize1.tail != tailAndSize2.tail:
        return None

    # set shorter and longer lists
    shorter = node()
    longer = node()
    if tailAndSize1.size > tailAndSize2.size:
        shorter = list2
        longer = list1
    else:
        shorter = list1
        longer = list2

    # move the pointer for the longer list by difference in lengths
    longer = getKthNode(longer, abs(tailAndSize2.size - tailAndSize1.size))

    # move both pointers until we have a collision
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    # return one the nodes
    return shorter

def getTailAndSize(n: node):
    if n is None:
        return None

    current = n
    count = 0

    while current.next is not None:
        count += 1
        current = current.next

    return tailAndSize(current, count)

def getKthNode(head: node, k):
    current = head
    while k > 0 and current is not None:
        current = current.next
        k -= 1
    return current

list1 = node(3)
list1.next = node(1)
list1.next.next = node(5)
list1.next.next.next = node(9)
list1.next.next.next.next = node(7)
list1.next.next.next.next.next = node(2)
list1.next.next.next.next.next.next = node(1)

list2 = node(4)
list2.next = node(6)
list2.next.next = list1.next.next.next


intersectingNode = findIntersection(list1, list2)
if intersectingNode is not None:
    print(intersectingNode.data)
else:
    print("No intersection")

