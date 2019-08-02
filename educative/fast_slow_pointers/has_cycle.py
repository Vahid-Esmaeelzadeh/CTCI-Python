class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def find_cycle_start(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            current = head
            while current != slow:
                current = current.next
                slow = slow.next
            return current

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print("LinkedList has cycle: " + str(has_cycle(head)))
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))
print("LinkedList cycle start: " + str(find_cycle_start(head).value))
