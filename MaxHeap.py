"""
Implement maxheap algorithm in Python
"""


def upAdjust(array):
    childrenIndex = len(array) - 1
    parentIndex = (childrenIndex - 1) // 2
    tmp = array[childrenIndex]
    while childrenIndex > 0 and tmp > array[parentIndex]:
        array[childrenIndex] = array[parentIndex]
        childrenIndex = parentIndex
        parentIndex = (parentIndex-1) // 2
    array[childrenIndex] = tmp
    return array


def downAdjust(array, parentIndex, length):
    """
    :param array: The heap represented by array
    :param parentIndex: Index for parent node
    :param length: valid length of heap (nodes before leaves)
    :return: modified heap
    """
    tmp = array[parentIndex]
    childrenIndex = parentIndex * 2 + 1
    while childrenIndex < length:
        if childrenIndex + 1 < length and array[childrenIndex] < array[childrenIndex+1]:
            childrenIndex += 1
        if tmp >= array[childrenIndex]:
            break
        array[parentIndex] = array[childrenIndex]
        parentIndex = childrenIndex
        childrenIndex = 2*childrenIndex + 1
    array[parentIndex] = tmp
    return array


def buildHeap(array):
    for i in range(len(array)-1, -1, -1):
        array = downAdjust(array, i, len(array)-1)
    return array




