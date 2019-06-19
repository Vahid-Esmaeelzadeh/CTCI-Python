# Question 2.8 (Loop Detection)
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loopDetection(lst: node):
    if lst is None:
        return None

    nodes = set()  # to save the  running nodes
    current = lst
    while current:
        if current not in nodes:  # it is a new node, add it to the set, and go forward
            nodes.add(current)
            current = current.next
        else:  # this is the looped node
            return current

    return None

def loopDetection2(head: node):
    slow = head
    fast = head

    # find the collision of fast and slow
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # collision
            break

    # check if there is no loop
    if (fast is None) or (fast.next is None):
        return None

    # move both pointers with the same pace and they will meet each other at loop start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # return one of slow/fast
    return slow

lst = node(1)
lst.next = node(2)
lst.next.next = node(3)
lst.next.next.next = node(4)
lst.next.next.next.next = node(5)
lst.next.next.next.next.next = lst.next.next.next

loopNode = loopDetection(lst)
if loopNode is not None:
    print(loopNode.data)
else:
    print("No loop")

loopNode = loopDetection2(lst)
if loopNode is not None:
    print(loopNode.data)
else:
    print("No loop")

