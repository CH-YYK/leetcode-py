class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        """
        O(N) in time, O(N) in space
        """
        if x < 0:
            return False
        # deduce the units from the integer and store them in a list
        res = []
        while x > 0:
            res.append(x % 10)
            x //= 10

        i = 0
        j = len(res) - 1
        while i < j:
            if res[i] != res[j]:
                return False
            else:
                i += 1
                j -= 1
        return True



