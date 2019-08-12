'''
Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
pixels to be stored in one byte.The screen has width w, where w is divisible by 8 (that is, no byte will
be split across rows). The height of the screen, of course, can be derived from the length of the array
and the width. Implement a function that draws a horizontal line from (xl, y) to (x2, y).
The method signature should look something like:


      x1      x2
      |       |
    bbbbbbbb_bbbbbbbb_bbbbbbbb_bbbbbbbb
    bbbbbbbb_bbbbbbbb_bbbbbbbb_bbbbbbbb
    bbbbbbbb_bbbbbbbb_bbbbbbbb_bbbbbbbb
y - bbbbbbbb_bbbbbbbb_bbbbbbbb_bbbbbbbb
    bbbbbbbb_bbbbbbbb_bbbbbbbb_bbbbbbbb
    bbbbbbbb_bbbbbbbb_bbbbbbbb_bbbbbbbb


drawLine(byte[] screen, int width, int xl, int x2, int y)
'''




def drawLine(screen, width: int, x1: int, x2: int, y: int):

    bitIndex1 = y * width + x1
    bitIndex2 = y * width + x2

    byteIndex1 = bitIndex1 // 8
    byteIndex2 = bitIndex2 // 8

    byteOffset1 = 7 - x1 % 8
    byteOffset2 = 7 - x2 % 8

    i = byteIndex1
    # [bbb11111] if i == 4
    screen[i] = (1 << (byteOffset1 + 1)) - 1

    # fill all bytes in between the first byte and last byte with 0xff
    i += 1
    while i < byteIndex2:
        screen[i] = 0xff
        i += 1

    # fill the last byte
    if byteIndex2 == byteIndex1:  # start and end are in the same byte
        screen[byteIndex2] &= (0xff ^ ((1 << byteOffset2) - 1))  # preserve the first update
    else:
        #screen[byteIndex2] = (0xff ^ ((1 << byteOffset2) - 1))
        screen[byteIndex2] = 0xff << byteOffset2


a = [0] * 40
drawLine(a, 64, 7, 9, 3)
for x in a:
    print(bin(x))

