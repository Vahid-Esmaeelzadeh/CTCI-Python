'''
Sum LinkedLists: You have two numbers represented by a linked list,where each Node contains a single
digit. The digits are stored in reverse order,such that the 1's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9.That is,912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2.That is, 912.
'''

from Common.common import *


# region basic - iterative
def sumLists(l1: linkedList, l2: linkedList):
    i1 = l1.head
    i2 = l2.head
    result = linkedList()
    carry = 0

    while i1 and i2:
        sum_val = i1.data + i2.data + carry
        s = sum_val % 10
        carry = sum_val // 10  # integer division
        result.addLast(Node(s))
        i1 = i1.next
        i2 = i2.next

    if i1 is None:
        while i2:
            sum_val = i2.data + carry
            s = sum_val % 10
            carry = sum_val // 10
            result.addLast(Node(s))
            i2 = i2.next

    if i2 is None:
        while i1:
            sum_val = i1.data + carry
            s = sum_val % 10
            carry = sum_val // 10
            result.addLast(Node(s))
            i1 = i1.next

    if carry > 0:
        result.addLast(Node(carry))

    return result
# endregion


# region basic - recursive
def sumLists_recursive(l1: linkedList, l2: linkedList):
    return linkedList(sumLists_helper(l1.head, l2.head, 0))


def sumLists_helper(n1: Node, n2: Node, carry):
    if n1 is None and n2 is None and carry == 0:
        return None

    result = Node()
    sum_val = carry

    if n1:
        sum_val += n1.data
    if n2:
        sum_val += n2.data

    result.data = sum_val % 10
    # recursive section
    next1 = None
    next2 = None
    if n1:
        next1 = n1.next
    if n2:
        next2 = n2.next

    more = sumLists_helper(next1, next2, sum_val // 10)
    result.next = more

    return result
# endregion


# region FOLLOW UP - CTCI solution
class partialSum:
    sum_list: Node = None  # to keep the linked list of partial sum
    carry = 0


def addLists(l1: linkedList, l2: linkedList):
    diff = l1.size() - l2.size()
    if diff > 0:
        l2 = padList(l2, diff)
    if diff < 0:
        l1 = padList(l1, -diff)

    # now, we have same length lists
    n1 = l1.head
    n2 = l2.head

    # add lists
    pSum:partialSum = addLists_helper(n1, n2)

    if pSum.carry == 0:
        return linkedList(pSum.sum_list)
    else:  # insert a Node for carry at the first of linked list
        result = insertFirst(pSum.sum_list, pSum.carry)
        return linkedList(result)


def addLists_helper(n1: Node, n2: Node):
    if n1 is None and n2 is None:
        return partialSum()

    pSum = addLists_helper(n1.next, n2.next)

    val = n1.data + n2.data + pSum.carry
    n = Node(val % 10)  # create a new Node with the new value

    # add the new Node at first of list
    #if pSum.sum_list:
    n.next = pSum.sum_list
    pSum.sum_list = n

    pSum.carry = val // 10
    return pSum


def insertFirst(n: Node, val):
    newNode = Node(val)
    #if n is not None:
    newNode.next = n
    return newNode


def padList(lst: linkedList, padding):
    head = lst.head
    for i in range(padding):
        head = insertFirst(head, 0)

    return linkedList(head)
# endregion


l1 = linkedList(Node(7))
l1.add(Node(3))
l1.add(Node(2))

l2 = linkedList(Node(9))
l2.add(Node(3))
l2.add(Node(0))
l2.add(Node(6))
l2.add(Node(9))

l1.print()
l2.print()
sumLists(l1, l2).print()
sumLists_recursive(l1, l2).print()

addLists(l2, l2).print()


print("-----------------------------")
num1 = Node(1)
num1.next = Node(2)
num1.next.next = Node(3)

num2 = Node(0)
num2.next = Node(1)
#num2.next.next = Node(3)

result = sum_lists(num1, num2)
result.print_list()

