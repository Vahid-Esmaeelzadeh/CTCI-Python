'''
Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to
generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
this task.

FOLLOW UP
What if you have only 1O MB of memory? Assume that all the values are distinct and we now have
no more than one billion non-negative integers.

Working with Files
Working with random functions
'''

from random import randint


def create_file(filename: str, total_num: int):
    N = total_num - 1
    f = open(filename, "w")
    k = 0
    while True:
        n = randint(0, N)
        f.write(str(n) + "\n")
        k = k + 1
        if k == total_num:
            f.close()
            break


# region part 1
def find_unused_number(filename: str):
    f = open(filename, "r")
    bit_field = [False] * (1 << 20)

    while True:
        line = f.readline()
        if line == '':
            break
        bit_field[int(line)] = True

    for i in range(len(bit_field)):
        if bit_field[i] is False:
            return i
# endregion


# region part 2
def find_open_number(filename: str):
    block_size = 1 << 20  # 2^20 bits < 10MB = 2^26

    # get number of values inside of each block
    blocks = get_count_per_block(filename, block_size)
    # find the block with missing number
    block_index = find_block_with_missing(blocks, block_size)
    if block_index < 0:
        return -1

    bit_vector = get_bit_vector_for_a_block(filename, block_index, block_size)


def get_count_per_block(filename, block_size):
    blocks_count = (1 << 31) // block_size + 1
    blocks = [0] * blocks_count

    f = open(filename, "r")
    while True:
        line = f.readline()
        if line == '':
            break
        blocks[int(line) // block_size] += 1

    f.close()
    return blocks


def find_block_with_missing(blocks, block_size):
    for i in range(len(blocks)):
        if blocks[i] < block_size:
            return i

    return -1


def get_bit_vector_for_a_block(filename, block_index, block_size):
    return
# endregion




create_file("large_file", 2 ** 20)
#open_num = find_unused_number("large_file")
#print(open_num)

