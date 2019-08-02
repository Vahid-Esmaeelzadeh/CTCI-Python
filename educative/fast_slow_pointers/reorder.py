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


def reorder(head: Node):
    if head is None or head.next is None or head.next.next is None:
        return

    slow = head
    fast = head
    tail_first_half = None

    while fast and fast.next:
        tail_first_half = slow
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)
    tail_first_half.next = head_second_half

    while head_second_half:
        next = head.next
        next2 = head_second_half.next
        tail = tail_first_half

        head.next = head_second_half
        head_second_half.next = next
        tail_first_half.next = next2

        head = next
        head_second_half = next2
        tail_first_half = tail


def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)
reorder(head)
head.print_list()

