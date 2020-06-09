# 5425. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

def maxArea(h: int, w: int, horizontalCuts, verticalCuts) -> int:
    horizontalCuts.sort()
    verticalCuts.sort()

    maxV = max(verticalCuts[0], w-verticalCuts[-1])
    for i in range(0, len(verticalCuts) - 1):
        maxV = max(maxV, verticalCuts[i + 1] - verticalCuts[i])

    maxH = max(horizontalCuts[0], h-horizontalCuts[-1])
    for i in range(0, len(horizontalCuts) - 1):
        maxH = max(maxH, horizontalCuts[i + 1] - horizontalCuts[i])

    return (maxH * maxV) % (pow(10,9) + 7)

h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]

print(maxArea(h, w, horizontalCuts, verticalCuts))

