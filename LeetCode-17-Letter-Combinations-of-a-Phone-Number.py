class Solution:
    # Iterative solution with O(N) and O(N)
    def letterCombinations(self, digits: str) -> 'List[str]':
        if not digits:
            return []
        corpus = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                    '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'}
    
        chars = [corpus[i] for i in digits]
        stack = list(chars[0])[::-1]
        res = []
        while stack:
            curr_chars = stack.pop()
            if len(curr_chars) == len(chars):
                res.append(curr_chars)
                continue
            for i in chars[len(curr_chars)][::-1]:
                stack.append(curr_chars + i)
        return res

class Solution2:
    # recursive solution with O(N) and O(N)
    def letterCombinations(self, digits):
        if not digits: 
            return []
        corpus = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                    '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'}
        return self.helper(digits, corpus)

    def helper(self, digits, corpus):
        if not digits:
            return ['']
        res = []
        for i in corpus[digits[0]]:
            res += [i + j for j in self.helper(digits[1:], corpus)]
        return res

if __name__ == "__main__":
    print(Solution2().letterCombinations('23'))

