'''
Palindrome: Implement a function to check if a linked list is a palindrome.
'''

from Common.common import *
import copy
# Question 2.6 (Palindrome)
'''
- we can use the size of list.
- we use a stack to push the first half of list in the stack
- we check the second half by popping the values from stack
'''
def isPalindrome(ll: linkedList) -> bool:

    listSize = ll.size()
    current = ll.head
    stk = []

    for i in range(listSize // 2):
        stk.append(current.data)
        # i += 1
        current = current.next

    if listSize % 2 == 1:  # skip the middle Node
        current = current.next

    while current is not None:
        if current.data != stk.pop():
            return False
        current = current.next

    if len(stk) == 0:
        return True

'''
reverse and compare
'''
def is_palidrome1(head: Node):
    rev = reverse_and_clone(head)
    return is_equal(head, rev)


def reverse_and_clone(node):
    head = None
    while node:
        n = Node(node.data)
        n.next = head
        head = n
        node = node.next

    return head


def is_equal(one: Node, two: Node):
    while one and two:
        if one.data != two.data:
            return False
        one = one.next
        two = two.next

    return (one is None) and (two is None)
'''
- We don't know the size of linkedlist
- We use two pointers (slow and fast) 
'''

def isPalindrome2(ll: linkedList):

    slow = ll.head
    fast = ll.head
    stk = []

    while fast and fast.next:
        stk.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:  # skip the middle Node
        slow = slow.next

    while slow is not None:
        if slow.data != stk.pop():
            return False
        slow = slow.next

    if len(stk) == 0:
        return True


'''
Recursive approach
- We can check the head and tail value, recall the function with the list after removing the head and tail
- Base case: if list.head is None or list.head.next is None ==> return True
'''


def isPalindrome_recr(ll: linkedList) -> bool:
    if ll.head is None or l1.head.next is None:
        return True

    current = ll.head
    prev = Node()  # use the prev pointer to be able to remove the last Node
    runner = ll.head

    while runner.next is not None:
        prev = runner
        runner = runner.next

    if current.data != runner.data:
        return False

    ll.head = ll.head.next  # remove the first item
    prev.next = runner.next

    return isPalindrome_recr(ll)


l1 = linkedList(Node(1))
l1.add(Node(2))
l1.add(Node(5))
l1.add(Node(2))
l1.add(Node(1))

print(isPalindrome(l1))
print(isPalindrome2(l1))
print(isPalindrome_recr(copy.deepcopy(l1)))

n = Node(1)
n.next = Node(2)
n.next.next = Node(3)
n.next.next.next = Node(4)
n.next.next.next.next = Node(1)

print(is_palidrome1(n))