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

print(stk1.min(), " -- ", stk2.min())
print(stk1.pop(), " -- ", stk2.pop())
print(stk1.min(), " -- ", stk2.min())
print(stk1.peek(), " -- ", stk2.peek())
# endregion
