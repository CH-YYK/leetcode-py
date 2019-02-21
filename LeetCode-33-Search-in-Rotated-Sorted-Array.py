class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # finding starting index with binary search
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        n = len(nums)
        lag = left
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            realmid = (mid + lag) % n
            print(realmid)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == '__main__':
    print(Solution().search(nums=[3,1], target=3))




