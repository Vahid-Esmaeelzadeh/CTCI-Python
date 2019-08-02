class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def print_list(self):
        temp = self
        while temp:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def addLast(self, item):
        if self.head is None:
            self.head = item
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = item
    def add(self, item):
        item.next = self.head
        self.head = item
    def remove(self):
        if self.head is not None:
            current = self.head
            self.head = self.head.next
            return current

    def peek(self):
        if self.head is not None:
            return self.head

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    def print(self):
        current = self.head
        print("[ ", end="")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("]")
