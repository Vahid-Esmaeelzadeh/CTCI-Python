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
