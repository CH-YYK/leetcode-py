class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2 = len(nums1) - len(nums2), len(nums2)
        r1, r2 = n1-1, n2-1
        curr = len(nums1) - 1
        while r1 >= 0 and r2 >= 0:
            if nums1[r1] > nums2[r2]:
                nums1[curr] = nums1[r1]
                r1 -= 1
            else:
                nums1[curr] = nums2[r2]
                r2 -= 1
            curr -= 1

        while r1 >= 0:
            nums1[curr] = nums1[r1]
            r1 -= 1
            curr -= 1

        while r2 >= 0:
            nums1[curr] = nums1[r1]
            r1 -= 1
            curr -= 1