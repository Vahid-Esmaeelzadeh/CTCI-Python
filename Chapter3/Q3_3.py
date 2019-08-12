'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific substack.
'''


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

