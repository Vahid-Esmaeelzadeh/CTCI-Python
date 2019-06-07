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
