class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        self.all = []
        self.dfs(nums, [])
        return self.all

    def dfs(self, nums, comb):
        if not nums:
            self.all.append(comb)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], comb + [nums[i]])

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))