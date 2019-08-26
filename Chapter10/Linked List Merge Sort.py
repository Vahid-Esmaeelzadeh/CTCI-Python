'''
merge sort linkedlist
'''


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def merge_sort(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Now, slow is the head of second half of list
    second_half_head = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(second_half_head)

    return merge(left, right)


def merge(left, right):
    h1 = left
    h2 = right
    result = Node()

    r = result

    while h1 or h2:
        if h1 is None:
            r.next = h2
            h2 = h2.next
        elif h2 is None:
            r.next = h1
            h1 = h1.next
        elif h1.val < h2.val:
            r.next = h1
            h1 = h1.next
        else:
            r.next = h2
            h2 = h2.next

        r = r.next

    return result.next


head = Node(10)
head.next = Node(1)
head.next.next = Node(5)
head.next.next.next = Node(-3)

result = merge_sort(head)
n = result
while n:
    print(n.val, end='->')
    n = n.next

print()



