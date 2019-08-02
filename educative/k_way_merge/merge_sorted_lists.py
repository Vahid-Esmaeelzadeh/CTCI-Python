'''
Merge K Sorted Lists
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
'''

from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for min-heap
    def __lt__(self, other):
        return self.value < other.value


def merge_lists2(lists):
    min_heap = []

    # push the first elements in the min-heap (smallest numbers)
    for r in lists:
        if r:
            heappush(min_heap, r)

    result_head, result_tail = None, None

    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    while min_heap:
        # pop the first element
        node = heappop(min_heap)

        # add at the end of result linked list
        if result_head is None:
            result_head = result_tail = node
        else:
            result_tail.next = node
            result_tail = result_tail.next

        # add the next node of the inserted node to the min-heap
        if node.next:
            heappush(min_heap, node.next)

    return result_head


def merge_lists(lists):
    result_head = None
    min_heap = []

    lists_currents = []
    for i in range(len(lists)):
        heappush(min_heap, (lists[i].value, i))
        lists_currents.append(lists[i].next)

    val, index = heappop(min_heap)
    result_head = ListNode(val)
    result_current = result_head

    heappush(min_heap, (lists_currents[index].value, index))
    lists_currents[index] = lists_currents[index].next

    while len(min_heap) > 0:
        val, index = heappop(min_heap)
        result_current.next = ListNode(val)

        if lists_currents[index]:
            heappush(min_heap, (lists_currents[index].value, index))
            lists_currents[index] = lists_currents[index].next

        result_current = result_current.next

    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)
    l1.next.next.next = ListNode(10)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists2([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
