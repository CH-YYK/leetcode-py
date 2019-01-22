"""
You are given an array, build a function to return the list of values from the array
O(1) O(1)
"""


class Solution:
    def findMode(self, array):
        if not array:
            return []
        maxAmount, integer, current, res = 1, array[0], 1, []
        for num in array[1:]:
            if num == integer:
                current += 1
            else:
                if current > maxAmount:
                    maxAmount = current
                    res = [integer]
                elif current == maxAmount:
                    res.append(integer)
                current = 1
            integer = num

        if current > maxAmount:
            return [num]
        elif current == maxAmount:
            return res + [num]
        else:
            return res


if __name__ == '__main__':
    array = [1, 1, 2, 2, 3, 4, 5]
    print(Solution().findMode(array))



