"""
    Find the size of overlapping area of two rectangles. You are provided the bottom-left and top-right points for each
    rectangle.
"""


class Solution:
    def areaOverlapping(self, Rb1, Rt1, Rb2, Rt2):
        height = self.distance(Rb1[0], Rt1[0], Rb2[0], Rt2[0])
        if height <= 0:
            return 0
        width = self.distance(Rb1[1], Rt1[1], Rb2[1], Rt2[1])
        if height <= 0:
            return 0
        return height * width

    def distance(self, Rb1, Rt1, Rb2, Rt2):
        return min(Rt1, Rt2) - max(Rb1, Rb2)


if __name__ == '__main__':
    Rb1 = (2, 1)
    Rb2 = (3, 2)
    Rt1 = (5, 5)
    Rt2 = (5, 7)
    print(Solution().areaOverlapping(Rb1, Rt1, Rb2, Rt2))