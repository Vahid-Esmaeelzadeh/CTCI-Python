# region Question 3.1 (Three in One)
class fixedMultiStack:

    def __init__(self, stackSize: int):
        self.numberOfStacks = 3
        self.stackCapacity = stackSize
        self.values = [None] * (stackSize * self.numberOfStacks)
        self.sizes = [0] * self.numberOfStacks

    def push(self, stackNum: int, value: int):
        if self.isFull(stackNum):
            print("Error! the stack is full.")
            return
        self.sizes[stackNum] += 1
        self.values[self.indexOfTop(stackNum)] = value


    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            print("Error! the stack is empty.")
            return

        value = self.values[self.indexOfTop(stackNum)]
        self.values[self.indexOfTop(stackNum)] = None
        self.sizes[stackNum] -= 1  # shrink

        return value

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            print("Error! the stack is empty.")
            return
        return self.values[self.indexOfTop(stackNum)]

    def isEmpty(self, stackNum: int) -> bool:
        return self.sizes[stackNum] == 0

    def isFull(self, stackNum: int) -> bool:
        return self.sizes[stackNum] == self.stackCapacity

    def indexOfTop(self, stackNum: int) -> int:
        return (stackNum * self.stackCapacity) + self.sizes[stackNum] - 1


print("----------- Q3.1 -----------")
multiStack1 = fixedMultiStack(3)
multiStack1.push(0, 1)
multiStack1.push(0, 2)
multiStack1.push(1, 4)
multiStack1.push(2, 7)

print(multiStack1.pop(0))
print(multiStack1.sizes)
print(multiStack1.pop(2))
print(multiStack1.sizes)
# endregion
# region Question 3.2 (Stack min)
import sys
class stackWithMin:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = []

    def push(self, val):
        if self.isFull():
            print("The  stack is full.")
            return

        newMin = min(val, self.min())
        self.values.append((val, newMin))

    def min(self):
        if len(self.values) == 0:
            return sys.maxsize
        return self.values[-1][1]  # The second item is the local min value

    def pop(self):
        return self.values.pop()[0]

    def isFull(self):
        if len(self.values) >= self.capacity:
            return True
        return False

    def peek(self):
        if len(self.values) == 0:
            print("The stack is empty.")
            return
        return self.values[-1][0]
class stackWithMin_opt:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = []
        self.minValues = []

    def push(self, val):
        if self.isFull():
            print("The stack is full.")
            return
        if val <= self.min():
            self.minValues.append(val)
        self.values.append(val)

    def isFull(self):
        if len(self.values) >= self.capacity:
            return True
        return False

    def pop(self):
        val = self.values.pop()
        if val == self.min():
            self.minValues.pop()
        return val

    def min(self):
        if len(self.minValues) == 0:
            return sys.maxsize
        return self.minValues[-1]

    def peek(self):
        if len(self.values) == 0:
            print("The stack is empty.")
            return
        return self.values[-1]


stk1 = stackWithMin(10)
stk2 = stackWithMin_opt(10)
stk1.push(2)
stk2.push(2)
stk1.push(3)
stk2.push(3)
stk1.push(4)
stk2.push(4)
stk1.push(1)
stk2.push(1)

print("----------- Q3.2 -----------")
print(stk1.min(), " -- ", stk2.min())
print(stk1.pop(), " -- ", stk2.pop())
print(stk1.min(), " -- ", stk2.min())
print(stk1.peek(), " -- ", stk2.peek())
# endregion
# region Question 3.3 (Stack of Plates)
class setOfStacks:
    def __init__(self, substackCapacity = 3, substacksCount = 2):
        self.substackCapacity = substackCapacity
        self.substacksCount = substacksCount
        self.substacks = [[]]
        self.currentSubStack = 0

    def push(self, value):
        if self.isFull():
            print("The stack is full.")
            return
        else:
            if len(self.substacks[self.currentSubStack]) < self.substackCapacity:  # there is at least one space in the current stack
                self.substacks[self.currentSubStack].append(value)
            else:  # we  need to create a new stack
                self.substacks.append([])
                self.currentSubStack += 1
                self.substacks[self.currentSubStack].append(value)

    def pop(self):
        if self.isEmpty():
            print("The stack is empty.")
            return
        elif len(self.substacks[self.currentSubStack]) > 0: # There is at least one element in the current stack to pop
            return self.substacks[self.currentSubStack].pop()
        else:
            self.currentSubStack -= 1
            del self.substacks[-1]  # the current stack is empty, and we have to remove it
            return self.substacks[self.currentSubStack].pop()


    def peek(self):
        if self.isEmpty():
            print("The stack is empty.")
            return
        return self.substacks[self.currentSubStack][-1]

    def isEmpty(self):
        if self.currentSubStack == 0 and len(self.substacks[0]) == 0:
            return True
        return False

    def isFull(self):
        if self.currentSubStack == self.substacksCount-1 and len(self.substacks[self.currentSubStack]) >= self.substackCapacity:
            return True
        return False

    def popAt(self, index):
        if len(self.substacks[index]) == 0:
            print("The substack is empty.")
        else:
            return self.substacks[index].pop()


setOfStacks1 = setOfStacks()
setOfStacks1.push(1)
setOfStacks1.push(2)
setOfStacks1.push(3)
setOfStacks1.push(4)
setOfStacks1.push(5)
setOfStacks1.push(6)
print(setOfStacks1.pop())
print(setOfStacks1.pop())
print(setOfStacks1.pop())
print(setOfStacks1.pop())
print(setOfStacks1.pop())
print(setOfStacks1.pop())
# endregion
# region Question 3.4 (Queue via Stacks)
class stackQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pushStack = []
        self.popStack = []

    def add(self, val):
        if self.isFull():
            print("The stackQueue is full.")
            return
        self.pushStack.append(val)

    def remove(self):
        if self.isEmpty():
            print("The stackQueue is empty.")
            return

        self.moveElements()
        return self.popStack.pop()

    def isEmpty(self):
        if len(self.pushStack) + len(self.popStack) == 0:
            return True
        return False

    def isFull(self):
        if len(self.pushStack) + len(self.popStack) >= self.capacity:
            return True
        return False

    def moveElements(self):
        if len(self.popStack) == 0:
            length = len(self.pushStack)
            for i in range(length):
                self.popStack.append(self.pushStack.pop())

stkQueue1 = stackQueue(10)
stkQueue1.add(1)
stkQueue1.add(2)
stkQueue1.add(3)
stkQueue1.add(4)
print(stkQueue1.remove())
print(stkQueue1.remove())
print(stkQueue1.remove())
print(stkQueue1.remove())
print(stkQueue1.remove())

# endregion
# region Question 3.5 (Sort Stack)
def sortStack(s1: list):
    s2 = []

    while len(s1) > 0:
        tmp = s1.pop()
        while len(s2) > 0 and s2[-1] > tmp:
            s1.append(s2.pop())
        s2.append(tmp)

    while len(s2) > 0:
        s1.append(s2.pop())

list1 = [10, -100, 3, 1.55, 7, -1, 2, 1]
sortStack(list1)
print(list1)
# endregion
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
            return self.cats.remove()
        if self.cats.size() == 0:
            return self.dog.remove()

        dog = self.dogs.peek()
        cat = self.cats.peek()

        if dog.order < cat.order:
            return self.dogs.remove()
        else:
            return self.cats.remove()

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



