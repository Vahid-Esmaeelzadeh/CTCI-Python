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

