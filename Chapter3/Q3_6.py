# region Question 3.6 (Animal Shelter)

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
            count += 1
            current = current.next
        return count

    def print(self):
        current = self.head
        print("[ ", end="")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("]")

class animal:
    def __init__(self, name: str):
        self.data = name
        self.next = None
        self.order = 0

class Dog(animal):
    def __init__(self, name: str):
        super().__init__(name)

class Cat(animal):
    def __init__(self, name: str):
        super().__init__(name)

class animalShelter:
    def __init__(self):
        self.cats = linkedList()
        self.dogs = linkedList()
        self.order = 0

    def enqueue(self, a: animal):
        a.order = self.order
        self.order += 1

        if isinstance(a, Dog):
            self.dogs.addLast(a)
        elif isinstance(a, Cat):
            self.cats.addLast(a)

    def dequeueAny(self):
        if self.dogs.size() == 0:
            return self.dequeueCat()
        if self.cats.size() == 0:
            return self.dequeueDog()

        dog = self.dogs.peek()
        cat = self.cats.peek()

        if dog.order < cat.order:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        return self.dogs.remove()

    def dequeueCat(self):
        return self.cats.remove()

shelter = animalShelter()
shelter.enqueue(Dog("dog1"))
shelter.enqueue(Cat("cat1"))
shelter.enqueue(Dog("dog2"))
shelter.enqueue(Dog("dog3"))
shelter.enqueue(Cat("cat2"))

print("%%%%, ", shelter.dequeueAny().data)
print("%%%%, ", shelter.dequeueDog().data)
print("%%%%, ", shelter.dequeueCat().data)
print("%%%%, ", shelter.dequeueAny().data)
print("%%%%, ", shelter.dequeueDog())




# endregion