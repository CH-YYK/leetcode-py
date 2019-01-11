"""
Given a graph, determine whether there is a path between two nodes
"""


class Solution:
    def pathInGraph(self, graph, start, end):
        tmp_graph = [[j for j in i] for i in graph]
        if self.helper(tmp_graph, start, end):
            return True
        return False

    def helper(self, graph, i, end):
        print(i+1)
        if i == end:
            return True
        resultset = []
        for next_ in range(len(graph[i])):
            if graph[i][next_] == 1:
                graph[next_][i] = 0
                graph[i][next_] = 0
                tmp = self.helper(graph, next_, end)
                if tmp:
                    return True
                resultset.append(tmp)
            else:
                continue
        if len(resultset) == 0:
            return False

if __name__ == '__main__':
    graph = [
        [0,1,0,0,1,0],
        [1,0,1,0,1,0],
        [0,1,0,1,0,0],
        [0,0,1,0,1,1],
        [1,1,0,1,0,0],
        [0,0,0,1,0,0]
    ]
    print(Solution().pathInGraph(graph, 4, 5))