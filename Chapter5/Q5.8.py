def drawLine(screen, width: int, x1: int, x2: int, y: int):
    numOfBytes = len(screen)
    height = numOfBytes/(width/8)

    bitIndex1 = y * width + x1
    bitIndex2 = y * width + x2

    byteIndex1 = bitIndex1 // 8
    byteIndex2 = bitIndex2 // 8

    byteOffset1 = 7 - x1 % 8
    byteOffset2 = 7 - x2 % 8

    i = byteIndex1
    screen[i] = (1 << (byteOffset1 + 1)) - 1

    i += 1
    while i < byteIndex2:
        screen[i] = 0xff
        i += 1

    if byteIndex2 == byteIndex1:
        screen[byteIndex2] &= (0xff ^ ((1 << byteOffset2) - 1))  # preserve the first update
    else:
        screen[byteIndex2] = (0xff ^ ((1 << byteOffset2) - 1))


a = [0] * 40
drawLine(a, 64, 7, 7, 3)

