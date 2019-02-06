class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        How long will it take to reach every node
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for u, v, w in times:
            graph[u] = graph.get(u, []) + [(w, v)]

        minTimeAccess = {i: float("inf") for i in range(1, N+1)}
        self.dfsHelper(K, 0, minTimeAccess, graph)
        res = max(minTimeAccess.values())
        return res if res < float("inf") else -1

    def dfsHelper(self, currNode, currTime, minTimeAccess, graph):
        if currTime >= minTimeAccess:
            return
        minTimeAccess[currNode] = currTime
        for w, v in sorted(graph[currNode]):
            self.dfsHelper(v, w + currTime, minTimeAccess, graph)

    def networkDelayTime2(self, times, N, K):  ## Dijkstra's Algorithm
        graph = {}
        for u, v, w in times:
            graph[u] = graph.get(u, []) + [(w, v)]

        dist = {i: float("inf") for i in range(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')

            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_node = i
                    cand_dist = dist[i]
            if cand_node == -1:
                break
            seen[cand_node] = True
            for w, v in graph.get(cand_node, []):
                dist[v] = min(dist[v], cand_dist + w)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTime3(self, times, N, K):  ## Dijkstra's Algorithm (Min heap)
        import heapq
        graph = {}
        for u, v, w in times:
            graph[u] = graph.get(u, []) + [(w, v)]
        heap = [(0, K)]
        dist = {}

        while heap:
            d, n = heapq.heappop(heap)
            if n in dist:
                continue
            dist[n] = d
            for dis, node in graph.get(n, []):
                if not node in dist:
                    heapq.heappush(heap, (d+dis, node))
        return max(dist.values()) if len(dist) == N else -1