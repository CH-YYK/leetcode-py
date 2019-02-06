class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        lessFromLeft = [0] * len(heights)
        lessFromRight = [0] * len(heights)
        lessFromLeft[0] = -1
        lessFromRight[-1] = len(heights)
        for i in range(len(heights)):
            p = i-1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p

        for i in range(len(heights) - 1, -1, -1):
            p = i + 1
            while p < len(heights) and heights[p] >= heights[i]:
                p = lessFromRight[p]
            lessFromRight[i] = p

        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, (lessFromRight[i]-lessFromLeft[i]-1) * heights[i])
        return maxArea