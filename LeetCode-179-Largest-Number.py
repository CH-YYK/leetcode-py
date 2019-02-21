class comparator:
    def __init__(self, obj):
        self.obj = obj

    def __lt__(self, other):
        return int(self.obj + other.obj) > int(other.obj + self.obj)

class Solution:
    def largestNumber(self, nums: 'List[int]') -> 'str':
        nums_str = [str(i) for i in nums]
        nums_str = sorted(nums_str, key=comparator)

        res = ""
        for i in range(len(nums_str)-1):
            if not res and nums_str[i] == '0':
                continue
            else:
                res += nums_str[i]
        res += nums_str[-1]
        return res


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    print(Solution().largestNumber(nums))