class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        if not nums1 or nums2:
            return []
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            while i + 1 < len(nums1) and nums1[i] == nums1[i+1]:
                i += 1
            while j + 1 < len(nums2) and nums2[j] == nums2[j+1]:
                j += 1

            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

if __name__ == '__main__':
    array1 = [1, 2, 2, 1]
    array2 = [2, 2]
    print(Solution().intersection(array1, array2))