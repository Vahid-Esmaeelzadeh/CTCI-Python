class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):
    if k <= 1:
        return head

    cur = head
    prv = None

    while cur:
        i = 1
        last_node_of_sub_list = cur
        last_node_of_previous_part = prv

        while cur and i <= k:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
            i += 1

        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = prv
        else:
            head = prv

        last_node_of_sub_list.next = cur
        prv = last_node_of_sub_list

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()


