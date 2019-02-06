class maxHeap(object):

    def __init__(self, nums):
        self.heap = self.buildHeap(nums)

    def upAdjust(self, array):
        chIndex = len(array) - 1
        pIndex = (chIndex - 1) // 2
        tmp = array[chIndex]
        while chIndex > 0 and tmp > array[pIndex]:
            array[chIndex] = array[pIndex]
            chIndex = pIndex
            pIndex = (chIndex - 1) // 2
        array[chIndex] = tmp
        return array

    def downAdjust(self, array, pIndex):
        tmp = array[pIndex]
        chIndex = pIndex * 2 + 1
        while chIndex < len(array):
            if chIndex + 1 < len(array) and array[chIndex] < array[chIndex+1]:
                chIndex += 1
            if tmp >= array[chIndex]:
                break
            array[pIndex] = array[chIndex]
            pIndex = chIndex
            chIndex = pIndex * 2 + 1
        array[pIndex] = tmp
        return array

    def buildHeap(self, array):
        for i in range(len(array) - 1, -1, -1):
            array = self.downAdjust(array, i)
        return array

if __name__ == '__main__':
    nums = [3,2,4,5,6,1]
    tmp = maxHeap(nums)
    print(tmp.heap)
