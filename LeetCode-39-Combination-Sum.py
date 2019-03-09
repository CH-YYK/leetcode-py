class Solution:
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        self.all = []
        self.helper(candidates, target, 0, [])
        return self.all

    def helper(self, candidates, target, i, path):
        if target == 0:
            self.all.append(path)
            return 
        if target < 0:
            return 
        for j in range(i, len(candidates)):
            self.helper(candidates, target-candidates[j], j, path + [candidates[j]])

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
        
        