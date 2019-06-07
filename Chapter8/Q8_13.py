# region Question 8.13 (Boxes)
# region --- my first try (need to be corrected)
def stackBoxes(remBoxes, selBoxes, height, heights):
    any_box_inserted = False
    for b in remBoxes:
        if check_and_insert_box(b, selBoxes):  # returns true if it is possible to insert
            any_box_inserted = True
            height += b[2]  # tuple(w, d, h)
            remBoxes.remove(b)  # remove the selected box from the remaining  boxes
            stackBoxes(remBoxes[:], selBoxes[:], height, heights)
        else:
            remBoxes.remove(b)

    if ~any_box_inserted:
        heights.append(height)


def check_and_insert_box(newBox, selBoxes):
    if len(selBoxes) == 0:
        selBoxes.append(newBox)
        return True

    for b in range(len(selBoxes)-1):
        if (len(selBoxes) == 1) and (newBox[0] > selBoxes[b][0]) and (newBox[1] > selBoxes[b][1]) and (newBox[2] > selBoxes[b][2]):
            selBoxes.insert(b, newBox)
            return True
        if (len(selBoxes) > 1) and (newBox[0] > selBoxes[b][0]) and (newBox[1] > selBoxes[b][1]) and (newBox[2] > selBoxes[b][2]) \
                and (newBox[0] < selBoxes[b+1][0]) and (newBox[1] < selBoxes[b+1][1]) and (newBox[2] < selBoxes[b+1][2]):

            selBoxes.insert(b, newBox)
            return True

    # check if it is smaller than all boxes
    if (newBox[0] < selBoxes[len(selBoxes)-1][0]) and (newBox[1] < selBoxes[len(selBoxes)-1][1]) and (newBox[2] < selBoxes[len(selBoxes)-1][2]):
        selBoxes.append(newBox)
        return True

    return False


newBox = (4, 4, 5)
selBoxes = [(3, 3, 2), (1, 0.5, 0.25)]
selBoxes1 = []
check_and_insert_box(newBox, selBoxes)
print(selBoxes)

boxes = [(30, 4, 2), (1, 0.5, 0.25), (4, 4, 5)]
#heights = []
#stackBoxes(boxes, [], 0, heights)
#print(heights)

boxes.sort(key=lambda x: x[2])
print(boxes)
# endregion
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

# region --- CTCI solution2
# endregion
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

# region --- CTCI solution3
# endregion
# endregion
