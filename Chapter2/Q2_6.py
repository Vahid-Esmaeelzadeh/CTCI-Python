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
        i += 1
        current = current.next

    if listSize % 2 == 1:  # skip the middle node
        current = current.next

    while current is not None:
        if current.data != stk.pop():
            return False
        current = current.next

    if len(stk) == 0:
        return True

'''
- We don't know the size of linkedlist
- We use two pointers (slow and fast) 
'''
def isPalindrome2(ll: linkedList):

    slow = ll.head
    fast = ll.head
    stk = []

    while fast is not None and fast.next is not None:
        stk.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:  # skip the middle node
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
    prev = node()  # use the prev pointer to be able to remove the last node
    runner = ll.head

    while runner.next is not None:
        prev = runner
        runner = runner.next

    if current.data != runner.data:
        return False

    ll.head = ll.head.next  # remove the first item
    prev.next = runner.next

    return isPalindrome_recr(ll)

l1 = linkedList(node(1))
l1.add(node(2))
l1.add(node(5))
l1.add(node(2))
l1.add(node(1))

print(isPalindrome(l1))
print(isPalindrome2(l1))
print(isPalindrome_recr(copy.deepcopy(l1)))

