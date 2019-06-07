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
    def add(self, item):
        item.next = self.head
        self.head = item
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

# region Question 2.5 (Sum lists)
def sumLists(l1: linkedList, l2:linkedList):
    i1 = l1.head
    i2 = l2.head
    result = linkedList()
    carry = 0

    while (i1 is not None) and (i2 is not None):
        sum_val = i1.data + i2.data + carry
        s = sum_val % 10
        carry = sum_val // 10  # integer division
        result.addLast(node(s))
        i1 = i1.next
        i2 = i2.next

    if i1 is None:
        while i2 is not None:
            sum_val = i2.data + carry
            s = sum_val % 10
            carry = sum_val // 10
            result.addLast(node(s))
            i2 = i2.next

    if i2 is None:
        while i1 is not None:
            sum_val = i1.data + carry
            s = sum_val % 10
            carry = sum_val // 10
            result.addLast(node(s))
            i1 = i1.next

    if carry > 0:
        result.addLast(node(carry))

    return result

def sumLists_recursive(l1: linkedList, l2: linkedList):
    return linkedList(sumLists_helper(l1.head, l2.head, 0))

def sumLists_helper(n1: node, n2: node, carry):
    if n1 is None and n2 is None and carry == 0:
        return None

    result = node()
    sum_val = carry

    if n1 is not None:
        sum_val += n1.data
    if n2 is not None:
        sum_val += n2.data

    result.data = sum_val % 10
    # recursive section
    next1 = None
    next2 = None
    if n1 is not None:
        next1 = n1.next
    if n2 is not None:
        next2 = n2.next

    more = sumLists_helper(next1, next2, sum_val // 10)
    result.next = more

    return result


class partialSum:
    sum_list: node = None  # to keep the linked list of partial sum
    carry = 0


def addLists(l1: linkedList, l2: linkedList):
    diff = l1.size() - l2.size()
    if diff > 0:
        l2 = padList(l2, diff)
    if diff < 0:
        l1 = padList(l1, -diff)

    n1 = l1.head
    n2 = l2.head

    # add lists
    pSum:partialSum = addLists_helper(n1, n2)

    if pSum.carry == 0:
        return linkedList(pSum.sum_list)
    else:  # insert a node for carry at the first of linked list
        result = insertFirst(pSum.sum_list, pSum.carry)
        return linkedList(result)


def addLists_helper(n1: node, n2: node):
    if n1 is None and n2 is None:
        pSum = partialSum()
        return pSum

    pSum = addLists_helper(n1.next, n2.next)

    val = n1.data + n2.data + pSum.carry
    n = node(val % 10)  # create a new node with the new value

    # add the new node at first of list
    if pSum.sum_list is not None:
        n.next = pSum.sum_list
    pSum.sum_list = n

    pSum.carry = val // 10
    return pSum


def insertFirst(n: node, val):
    newNode = node(val)
    if n is not None:
        newNode.next = n
    return newNode

def padList(lst: linkedList, padding):
    head = lst.head
    for i in range(padding):
        head = insertFirst(head, 0)

    return linkedList(head)

l1 = linkedList(node(7))
l1.add(node(3))
l1.add(node(2))

l2 = linkedList(node(9))
l2.add(node(3))
l2.add(node(0))
l2.add(node(6))
l2.add(node(9))

l1.print()
l2.print()
sumLists(l1, l2).print()
sumLists_recursive(l1, l2).print()

addLists(l1, l2).print()
# endregion
