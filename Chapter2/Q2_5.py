from Common.common import *

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

    # now, we have same length lists
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
        return partialSum()

    pSum = addLists_helper(n1.next, n2.next)

    val = n1.data + n2.data + pSum.carry
    n = node(val % 10)  # create a new node with the new value

    # add the new node at first of list
    #if pSum.sum_list:
    n.next = pSum.sum_list
    pSum.sum_list = n

    pSum.carry = val // 10
    return pSum


def insertFirst(n: node, val):
    newNode = node(val)
    #if n is not None:
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

addLists(l2, l2).print()
# endregion
