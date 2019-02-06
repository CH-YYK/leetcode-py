class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num & (num-1) == 0:
            while num > 1:
                num /= 4
            return num == 1
        else:
            return False

if __name__ == '__main__':
    print(Solution().isPowerOfFour(8))
