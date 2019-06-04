#region Question 2.1 (remove duplicates)
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

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


def removeDups(ll: linkedList):
    n = ll.head
    dataset = set([])
    prev = node()
    while n is not None:
        if n.data in dataset:
            prev.next = n.next
        else:
            dataset.add(n.data)
            prev = n
        n = n.next


l1 = linkedList(node(1))
l1.addLast(node(1))
l1.addLast(node(1))
l1.addLast(node(1))
l1.addLast(node(1))
l1.print()


removeDups(l1)
l1.print()

#endregion
