class graph:
    def __init__(self, vertices, edges):
        self.v = vertices
        self.e = edges


class Solution:
    def DFSTraversal(self, graph):
        """
        O(length(e)+length(v))
        :param graph:
        :return:
        """
        v = graph.v
        e = graph.e
        visited = {}
        traversal = []
        for vertex in v:
            if vertex not in visited:
                self.visit(vertex, visited, e, traversal)
        return traversal

    def visit(self, vertex, visited, edges, traversal):
        visited[vertex] = True
        traversal.append(vertex)
        for nextVertex in edges[vertex]:
            if nextVertex not in visited:
                self.visit(nextVertex, visited, edges, traversal)


class Solution2:
    def DFSTraversal(self, graph):
        if not graph:
            return []
        v = graph.v
        e = graph.e
        visited = {}
        stack = []
        traversal = []

        for vertex in v:
            if vertex not in visited:
                stack.append(vertex)
                while stack:
                    curr = stack.pop()
                    if curr in visited:
                        continue
                    visited[curr] = True
                    traversal.append(curr)
                    for nextVertex in e[curr][::-1]:
                        if nextVertex not in visited:
                            stack.append(nextVertex)
        return traversal


if __name__ == '__main__':
    v = [1, 2, 3, 4]
    e = {
        1: [3, 4],
        2: [3, 4],
        3: [1, 2, 5],
        4: [1, 2],
        5: [3]
    }
    g = graph(v, e)
    ans = Solution2().DFSTraversal(g)
    print(ans)


