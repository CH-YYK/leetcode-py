class Solution:
    def longestPalindrome(self, s):
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1

        count = 0
        ind = 0
        for i in dic:
            if dic[i] % 2 == 0:
                count += dic[i]
            else:
                ind = 1
                count += dic[i] - 1
        return count + ind

if __name__ == '__main__':
    s = "abccccdd"
    print(Solution().longestPalindrome(s))
