class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
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
    nums1 = [1,2,2,1]
    nums2 = [0,2,2,0]
    print(Solution().intersect(nums1, nums2))