'''
LinkedList Palindrome LinkedList(medium)
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm
is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


# without stack - space order = O(1)
def is_palindromic_linked_list2(head):
    if head is None or head.next is None:
        return True

    # find the middle of linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half
    head_second_half = reverse(slow)
    # store the head of reversed list to retrieve the original one
    copy_head_second_half = head_second_half

    while head and head_second_half:
        if head.value != head_second_half.value:
            break

        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)

    if head is None or head_second_half is None:
        return True

    return False

'''
reverse linkedlist
'''


def reverse(head):
    if head is None or head.next is None:
        return head

    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


# using stack and slow and fast pointers
def is_palindromic_linked_list(head):
    slow = head
    fast = head

    items = []
    while fast and fast.next:
        items.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    # Now, slow is the middle of list

    # move it one node  forward if the length of list is odd
    if fast:
        slow = slow.next

    while slow:
        if items.pop() != slow.value:
            return False
        slow = slow.next

    return True


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)

print("Is palindrome: " + str(is_palindromic_linked_list(head)))
print("Is palindrome: " + str(is_palindromic_linked_list2(head)))
head.print_list()

head.next.next.next.next.next = Node(2)
print("Is palindrome: " + str(is_palindromic_linked_list(head)))
print("Is palindrome: " + str(is_palindromic_linked_list2(head)))

head.print_list()