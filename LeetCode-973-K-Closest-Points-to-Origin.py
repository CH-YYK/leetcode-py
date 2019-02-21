class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        for i in range(len(points)):
            points[i] += [self.distance(*points[i])]
        points.sort(key=lambda x: x[-1])
        return [i[:-1] for i in points[:K]]

    def distance(self, x, y):
        return x**2 + y**2

    def kClosest2(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        import heapq
        res = []
        heap = []
        for i in range(0, len(points)):
            heap.append((self.distance(*points[i]), points[i]))

        heapq.heapify(heap)
        while len(res) < K:
            res.append(heapq.heappop(heap)[1])
        return res

