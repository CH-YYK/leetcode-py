"""
Give a string, build a function to return all its character permutations
"""


class Solution:
    def stringPermutation(self, string):
        all_list = []
        self.permutation(string, "", all_list)
        return all_list

    def permutation(self, string, prefix, all):
        if len(string) == 0:
            all.append(prefix)
        else:
            for i in range(len(string)):
                remain = string[:i] + string[i+1:]
                self.permutation(remain, prefix + string[i], all)


if __name__ == '__main__':
    solution = Solution()
    print(solution.stringPermutation("abc"))