'''
HashMap implementation
HashTable implementation
'''


from collections import deque


class LinkedListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None


class HashTable:
    def __init__(self, capacity=100):
        self.arr = [None for _ in range(capacity)]
        self.capacity = capacity
        self.length = 0

    def get_index_for_key(self, key):
        return hash(key) % self.capacity

    def get_node_for_key(self, key):
        index = self.get_index_for_key(key)
        if index < len(self.arr):
            current = self.arr[index]

            while current:
                if current.key == key:
                    return current
                current = current.next

        return None

    # get value for key
    def get(self, key):
        node = self.get_node_for_key(key)
        if node:
            return node.value
        return None

    def remove(self, key):
        node = self.get_node_for_key(key)
        if node:
            if node.prev:
                node.prev.next = node.next
            else:
                hashKey = self.get_index_for_key(key)
                self.arr[hashKey] = node.next

            if node.next:
                node.next.prev = node.prev

            self.length -= 1

    def put(self, key, value):
        node = self.get_node_for_key(key)
        if node:  # already there
            node.value = value
            return

        node = LinkedListNode(key, value)
        index = self.get_index_for_key(key)

        if self.arr[index]:  # we have a LinkedList for the key
            node.next = self.arr[index]  # put the new node at the beginning of Linked List
            node.next.prev = node

        self.arr[index] = node
        self.length += 1

    def __len__(self):
        return self.length


ht = HashTable()
ht.put("Vahid", "$10M")
ht.put("Elahesadat", "$12M")
ht.put("Elahe", "$56M")

print(len(ht))

print(ht.get("Elahesadat"))

print(ht.get("Vahid"))
ht.put("Vahid", "$25M")
print(ht.get("Vahid"))
ht.remove("Vahid")
print(ht.get("Vahid"))

print(ht.get("Elahe"))
print(len(ht))

