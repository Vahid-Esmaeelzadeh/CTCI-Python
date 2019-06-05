#region Question 2.1 (remove duplicates)
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def addLast(self, item):
        if self.head is None:
            self.head = item
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = item

    def remove(self):
        if self.head is not None:
            current = self.head
            self.head = self.head.next
            return current

    def peek(self):
        if self.head is not None:
            return self.head

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    def print(self):
        current = self.head
        print("[ ", end="")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("]")


def removeDups(ll: linkedList):
    n = ll.head
    dataset = set()
    prev = node()
    while n is not None:
        if n.data in dataset:
            prev.next = n.next
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

# region Question 2.2 (Return Kth to Last)
def kLast_basic(ll:linkedList, k:int):
    N = ll.size()
    if k > N or k < 0:
        return None

    itemNum = N - k
    i = 1
    current = ll.head
    while (current is not None) and i != itemNum:
        i += 1
        current = current.next
    return current.data

def kLast_recr(ll:linkedList, k:int):
    kLast_helper(ll.head, k)

def kLast_helper(n: node, k: int):
    if n is None:
        return 0
    index = kLast_helper(n.next, k) + 1
    if index == k:
        print(k, "th to the last node is ", n.data)
    return index

def kLast(ll: linkedList, k:int):
    if k <= 0:
        return None

    current = ll.head
    runner = ll.head
    i = 0

    while i < k:
        if runner is None:
            return None
        runner = runner.next
        i += 1
    while runner is not None:
        current = current.next
        runner = runner.next

    return current.data

ll = linkedList(node(1))
ll.addLast(node(2))
ll.addLast(node(3))
ll.addLast(node(4))
ll.addLast(node(5))

item = kLast_basic(ll, -1)
kLast_recr(ll, 1)
print(kLast(ll, 0))

# endregion

# region Question 2.3 (delete middle node)
def deleteNode(n: node):
    if n is None or n.next is None:
        return False

    nextNode:node = n.next
    n.data = nextNode.data
    n.next = nextNode.next

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

# region Question 2.4 (Partition)
import copy
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