'''
21. Merge Two Sorted Lists
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next

        current = head

        while l1 and l2:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return head


list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(-10)
list2.next = ListNode(2)


sol = Solution()
mlist = sol.mergeTwoLists(list1, list2)
while mlist:
    print(mlist.val, end=" ")
    mlist = mlist.next