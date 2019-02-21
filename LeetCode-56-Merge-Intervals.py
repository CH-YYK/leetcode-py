# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        i = 1

        while i < len(intervals):
            preInterval = res[-1]
            currInterval = intervals[i]

            if preInterval.end < currInterval.start:
                res.append(currInterval)
            else:
                lower = min(preInterval.start, currInterval.start)
                upper = max(preInterval.end, currInterval.end)
                res[-1].start = lower
                res[-1].end = upper
            i += 1
        return res

    def merge2(self, intervals: 'List[Interval]') -> 'List[Interval]':
        # stack and queue
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x.start)
        stack = [intervals.pop(0)]
        while intervals:
            preInterval = stack.pop()
            currInterval = intervals.pop(0)

            if preInterval.end < currInterval.start:
                stack.append(preInterval)
                stack.append(currInterval)
            else:
                lower = min(preInterval.start, currInterval.start)
                upper = max(preInterval.end, currInterval.end)
                preInterval.start = lower
                preInterval.end = upper
                stack.append(preInterval)
        return stack

if __name__ == '__main__':
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10)]
    ans = Solution().merge(intervals)
    print([[i.start, i.end] for i in ans])