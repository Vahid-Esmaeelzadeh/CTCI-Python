# region Question 8.1 (countWays)
def countways1(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return countways1(n-1) + countways1(n-2) + countways1(n-3)

def countways2(n: int) -> int:
    memo = [None] * (n+1)
    return countways2_helper(n, memo)

def countways2_helper(n: int, memo: list):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] is None:
        memo[n] = countways1(n-1) + countways1(n-2) + countways1(n-3)
    return memo[n]

def countways3(n: int):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2

    c0 = 1
    c1 = 1
    c2 = 2
    count = 0

    for i in range(3, n+1):
        count = c0 + c1 + c2
        c0 = c1
        c1 = c2
        c2 = count

    return count

print(countways1(1))
print(countways2(1))
print(countways3(1))

#region Question 8.4 (power set)
def getAllSubsets(lst):
    if not lst:
        return [[]]
    outlist = getAllSubsets(lst[1:])
    '''
    for rest in outlist
        withFirst += lst[0] + rest
    '''
    withFirst = [[lst[0]] + rest for rest in outlist]
    withoutFirst = outlist
    return withoutFirst + withFirst


def powerset(lst):
    n = 1 << len(lst)
    allsubsets = []

    for i in range(n):
        subset = int2set(lst, i)
        allsubsets += [subset]
        #allsubsets.append(subset)
    return allsubsets
def int2set(lst, i):
    subset = []
    k = i
    index = 0
    while k > 0:
        if (k & 1) == 1:
            subset += [lst[index]]
            #subset.append(lst[index])
        index += 1
        k >>= 1
    return subset


set_in = [1, 2, 3]
print(getAllSubsets(set_in))
print (powerset(set_in))
#endregion
#region Question 8.5 (recursive multiply)


def recurMul (a, b):
    if a > b:
        return recurMulHelper(a, b, 0)
    else:
        return recurMulHelper(b, a, 0)


def recurMulHelper(a, b, i):
    if b == 0:
        return 0

    temp = 0
    if (b & 1) == 1:
        temp = a

    return (temp << i) + recurMulHelper(a, b >> 1, i+1)


print(recurMul(11,17))
#endregion
#region Question 8.6 (Hanoi Towers)
def moveDisks(n, origin, destination, buffer):
    if n <= 0:
        return
    moveDisks(n-1, origin,  buffer, destination)
    moveTop(origin, destination)
    moveDisks(n-1, buffer, destination, origin)


def moveTop(origin, destination):
    print("moving disk from ", origin, " to ", destination)

moveDisks(4, 'A', 'C', 'B')
#endregion
# region Question 8.7 (permutations)
def permutations(str):
    if len(str) == 0:
        return ['']

    prevList = permutations(str[1:])
    nextList = []

    for i in range(len(prevList)):
        for j in range(len(str)):
            newString = prevList[i][:j] + str[0] + prevList[i][j:]
            if newString not in nextList:
                nextList.append(newString)

    return nextList

strList = '\n'.join(permutations('aaab'))
print(strList)


#endregion
# region Question 8.8 (permutations dups)

def permutationsDup(str):
    freqTable = buildFreqTable(str)
    result = permutaionsDupHelper(freqTable)
    return result


def permutaionsDupHelper(freqTable):
    result = []
    for i in freqTable.keys():
        if freqTable[i] > 0:
            freqTable[i] = freqTable[i] - 1
            lst = permutaionsDupHelper(freqTable)
            for s in lst:
                result.append(freqTable[i] + s)
    return result

def buildFreqTable(str):
    freqTable = dict()
    for c in str:
        if c not in freqTable:
            freqTable[c] = 0;
        freqTable[c] = freqTable[c] + 1
    return freqTable



freqTable = buildFreqTable('baabcdd')
print(freqTable)

print(permutationsDup('abbccc'))
# endregion
# region Question 8.9 (parens)
def parens1(n):
    if n == 1:
        return ['()']

    lst = parens1(n-1)
    result = []
    for s in lst:
        # at the beginning
        newString = '()' + s
        if newString not in result:
            result.append(newString)
        # after each '('
        for j in range(len(s)):
            if s[j] == '(':
                newString = s[:j+1] + '()' + s[j+1:]
                if newString not in result:
                    result.append(newString)

    return result

print('\n'.join(parens1(4)))

# endregion
#region Question 8.10 (PaintFill)
def paintFill(canvas, newColor, r, c):
    if r < 0 or c < 0 or r >= len(canvas) or c >= len(canvas[0]):
        return
    paintFillHelper(canvas, newColor, r, c, canvas[r][c])


def paintFillHelper(canvas, newColor, r, c, selectedColor):
    if r < 0 or c < 0 or r >= len(canvas) or c >= len(canvas[0]):
        return
    if canvas[r][c] != selectedColor:
        return

    canvas[r][c] = newColor

    paintFillHelper(canvas, newColor, r + 1, c - 1, selectedColor)
    paintFillHelper(canvas, newColor, r + 1, c, selectedColor)
    paintFillHelper(canvas, newColor, r + 1, c + 1, selectedColor)
    paintFillHelper(canvas, newColor, r, c - 1, selectedColor)
    paintFillHelper(canvas, newColor, r, c + 1, selectedColor)
    paintFillHelper(canvas, newColor, r - 1, c - 1, selectedColor)
    paintFillHelper(canvas, newColor, r - 1, c, selectedColor)
    paintFillHelper(canvas, newColor, r - 1, c + 1, selectedColor)


canvas = [['R', 'R', 'R', 'R', 'R', 'R', 'R'],
          ['R', 'R', 'B', 'B', 'B', 'G', 'G'],
          ['B', 'B', 'G', 'G', 'G', 'R', 'R'],
          ['R', 'G', 'B', 'B', 'R', 'R', 'R'],
          ['B', 'B', 'B', 'R', 'B', 'R', 'G']]

paintFill(canvas, 'K', 2, 2)
print(canvas)
# endregion
# region Question 8.11 (coins)
def coins(n):
    if n <= 0:
        return 0
    return coinsHelper(n)

def coinsHelper(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return coinsHelper(n - 1) + coinsHelper(n - 5) + coinsHelper(n - 10) + coinsHelper(n - 25)


def count(S, m, n):
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <= 0 and n >= 1):
        return 0

    # count is sum of solutions
    # (i) excluding S[m-1] (ii) including S[m-1]
    return count(S, m - 1, n) + count(S, m, n - S[m - 1]);

def count_DP(S, m, n, memo):
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <= 0 and n >= 1):
        return 0

    if (m-1, n) not in memo:
        memo[(m-1, n)] = count_DP(S, m - 1, n, memo)

    if (m, n-S[m-1]) not in memo:
        memo[(m, n-S[m-1])] = count_DP(S, m, n - S[m - 1], memo)
    # count is sum of solutions
    # (i) excluding S[m-1] (ii) including S[m-1]
    return memo[(m-1, n)] + memo[(m, n-S[m-1])]


arr = [25, 10, 5, 1]
m = len(arr)
n = 120
memo = dict()
print(count(arr, m, n))
print(count_DP(arr, m, n, memo))
# endregion
# region Question 8.12 (8 queens)
import copy
def queens(n, chess):

    if n == 0:
        return 1
    if noWay(chess):
        return 0

    cell = find_smallest_cell(chess)
    # update the chess if we don't use the smallest cell
    chess1 = copy.deepcopy(chess)
    #chess1 = chess[:]
    chess1[cell] = -1
    # update the chess if we use the smallest cell
    chess2 = updateChess(chess, cell)
    return queens(n, chess1) + queens(n-1, chess2)


def noWay(chess):
    for i in range(8):
        for j in range(8):
            if chess[(i, j)] == 0:
                return False

    return True

def updateChess(chess, cell):
    chess2 = copy.deepcopy(chess)
    row = cell[0]
    col = cell[1]

    for i in range(8):
        for j in range(8):
            if i == row or j == col or abs(i-row) == abs(j-col):
                chess2[(i, j)] = -1
    return chess2


def find_smallest_cell(chess):
    for i in range(8):
        for j in range(8):
            if chess[(i, j)] == 0:
                return (i, j)


chess = {(x, y): 0 for x in range(8) for y in range(8)}

#print(queens(8, chess))
print(chess)

# endregion
# region Question 8.12 (8 queens - CTCI solution)
GRID_SIZE = 8
def placeQueens(row, columns, results):
    if row == GRID_SIZE:
        results.append(columns)
    else:
        for col in range(GRID_SIZE):
            if checkValid(columns, row, col):
                columns[row] = col
                placeQueens(row+1, columns[:], results)

def checkValid(columns, row1, column1):
    for row2 in range(row1):
        column2 = columns[row2]

        if column1 == column2:
            return False
        if abs(column2-column1) == (row1-row2):
            return False

    return True

columns = [None]*8
results = []

placeQueens(0, columns, results)
print(len(results))

for s in results:
    print(*s)
# endregion
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
# region Question 8.14 (Boolean Evaulation)


def boolEval(expr: str, result: bool) -> int:
    if len(expr) == 0:
        return 0
    if len(expr) == 1:
        return int(int(expr[0]) == int(result))

    ways = 0
    memo = dict()

    if (expr, result) in memo:
        return memo[(expr, result)]

    for i in range(1, len(expr), 2):
        leftTrue = boolEval(expr[:i], True)
        leftFalse = boolEval(expr[:i], False)
        rightTrue = boolEval(expr[i + 1:], True)
        rightFalse = boolEval(expr[i + 1:], False)

        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

        totalTrue = 0

        if expr[i] == '^':
            totalTrue = (leftTrue * rightFalse) + (leftFalse * rightTrue)
        elif expr[i] == '&':
            totalTrue = leftTrue * rightTrue
        elif expr[i] == '|':
            totalTrue = (leftTrue * rightTrue) + (leftFalse * rightTrue) + (leftTrue * rightFalse)

        if result:
            ways += totalTrue
        else:
            ways += total - totalTrue

    memo[(expr, result)] = ways
    return ways

print(boolEval("1^0&0&0&1^1|0&1|0", False))
# endregion