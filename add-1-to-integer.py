class Solution:
    def add_one(self, array):  # recursive solution
        res = []
        return self.helper(array, len(array)-1, 1, res)

    def helper(self, array, index, carry, res):
        if index < 0 and carry == 1:
            return [1] + res
        if index < 0:
            return res

        Sum = array[index] + carry
        if Sum >= 10:
            res = [Sum % 10]+res
            return self.helper(array, index-1, 1, res)
        else:
            res = [Sum] + res
            return self.helper(array, index-1, 0, res)

    def add_one2(self, array):  # iterative
        res = []
        carry = 1
        for i in range(len(array)-1, -1, -1):
            Sum = array[i] + carry
            if Sum >= 10:
                Sum %= 10
                carry = 1
            res = [Sum] + res
        if carry == 1:
            return [1] + res

if __name__ == '__main__':
    array = [9, 9, 9]
    print(Solution().add_one2(array))