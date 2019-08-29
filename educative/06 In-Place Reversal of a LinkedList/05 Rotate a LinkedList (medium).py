'''
Rotate a LinkedList

Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def size(self):
        temp = self
        n = 0
        while temp:
            temp = temp.next
            n += 1

        return n


# my solution
def rotate(head, rotations):
    n = head.size()
    rotations = rotations % n
    pivot = n - rotations

    if rotations <= 0 or head is None or head.next is None:
        return head

    previous, current = None, head
    i = 0
    start_of_first_sublist = current
    while i < pivot and current:
        previous = current
        current = current.next
        i += 1
    # previous points the last node of first sublist. We should change its next to None
    previous.next = None

    # current points the second sublist. It will be the head of new linkedlist
    head = current
    # move the current to the end of second sublist
    while current.next:
        current = current.next

    # current points the last node of second sublist
    current.next = start_of_first_sublist

    return head


# educative solution
def rotate2(head, rotations):
    if head is None or head.next is None or rotations <= 0:
        return head

    # find the length and the last node of the list
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1

    last_node.next = head  # connect the last node with the head to make it a circular list
    rotations %= list_length  # no need to do rotations more than the length of the list
    skip_length = list_length - rotations
    last_node_of_rotated_list = head
    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    # 'last_node_of_rotated_list.next' is pointing to the sub-list of 'k' ending nodes
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 2)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
