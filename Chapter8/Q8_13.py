'''
Stack of Boxes: You have a stack of n boxes, with widths wi, heights hi, and depths di. The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
'''


# region --- CTCI solution1
def createStack1(boxes):
    # sort the boxes based on the height in descending order
    boxes.sort(key=lambda x: x[2], reverse=True)
    maxHeight = 0
    for i in range(len(boxes)):
        height = createStackHelper1(boxes, i)
        maxHeight = max(height, maxHeight)
    return maxHeight


def createStackHelper1(boxes, buttomIndex):
    maxHeight = 0
    for i in range(buttomIndex + 1, len(boxes)):
        if compareBoxes(boxes[i], boxes[buttomIndex]):
            height = createStackHelper1(boxes, i)
            maxHeight = max(height, maxHeight)

    maxHeight += boxes[buttomIndex][2]
    return maxHeight


def compareBoxes(box1, box2):
    if (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2]):
        return True
    return False


boxes = [(3, 2, 2), (1, 10, 0.25), (4, 4, 1.5)]
print(createStack1(boxes))
# endregion


# region --- CTCI solution2 -- memoization
def createStack2(boxes):
    # sort the boxes based on the height in descending order
    boxes.sort(key=lambda x: x[2], reverse=True)
    maxHeight = 0
    for i in range(len(boxes)):
        height = createStackHelper2(boxes, i)
        maxHeight = max(height, maxHeight)
    return maxHeight


def createStackHelper2(boxes, buttomIndex):
    maxHeight = 0
    heights = dict()
    for i in range(buttomIndex + 1, len(boxes)):
        if compareBoxes(boxes[i], boxes[buttomIndex]):
            if i not in heights:
                height = createStackHelper1(boxes, i)
                heights[i] = height
            else:
                height = heights[i]
            maxHeight = max(height, maxHeight)

    maxHeight += boxes[buttomIndex][2]
    return maxHeight

print(createStack2(boxes))
# endregion
