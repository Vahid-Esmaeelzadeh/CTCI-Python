'''
Animal Shelter: An animal shelter, which holds only dogs andcats, operates on a strictly "first in, first
out"basis. People must adopt either the "oldest"(based on arrival time) ofall animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specifc animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat.You may use the built-in Linkedlist data structure.
'''

from collections import deque


# region using deque
class MyAnimal:
    def __init__(self, name):
        self.name = name
        self.order = 0


class MyDog(MyAnimal):
    def __init__(self, name):
        super().__init__(name)


class MyCat(MyAnimal):
    def __init__(self, name):
        super().__init__(name)


class Shelter:
    def __init__(self):
        self.cat_queue = deque()
        self.dog_queue = deque()
        self.order = 0

    def enqueue(self, a: MyAnimal):
        a.order = self.order
        self.order += 1

        if isinstance(a, MyDog):
            self.dog_queue.append(a)
        elif isinstance(a, MyCat):
            self.cat_queue.append(a)

    def dequeue_dog(self):
        if len(self.dog_queue) == 0:
            return None
        return self.dog_queue.popleft()

    def dequeue_cat(self):
        if len(self.cat_queue) == 0:
            return None
        return self.cat_queue.popleft()

    def dequeue_any(self):
        if len(self.cat_queue) == 0:
            return self.dequeue_dog()

        if len(self.dog_queue) == 0:
            return self.dequeue_cat()

        if self.cat_queue[0].order < self.dog_queue[0].order:
            return self.cat_queue.popleft()
        else:
            return self.dog_queue.popleft()
# endregion


# region with my own linkedList
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
# endregion

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

print("-----------------------")
shelter1 = Shelter()
shelter1.enqueue(MyDog("dog1"))
shelter1.enqueue(MyCat("cat1"))
shelter1.enqueue(MyDog("dog2"))
shelter1.enqueue(MyDog("dog3"))
shelter1.enqueue(MyCat("cat2"))

print("%%%%, ", shelter1.dequeue_any().name)
print("%%%%, ", shelter1.dequeue_dog().name)
print("%%%%, ", shelter1.dequeue_cat().name)
print("%%%%, ", shelter1.dequeue_any().name)
print("%%%%, ", shelter1.dequeue_dog())
