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


