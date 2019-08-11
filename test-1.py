sample_input = ['AB', 'BD', 'DC', 'CD', 'DA', 'AC']


class Solution:

    def findSeq(self, nodes):
        pre_fix = {}
        for node in nodes:
            if node[0] in pre_fix:
                pre_fix[node[0]].append(node)
            else:
                pre_fix[node[0]] = [node]
        
        node_index = {}
        graph = []
        for i, node in enumerate(nodes):
            graph.append(pre_fix[node[1]])
            node_index[node] = i
        
        self.graph = graph
        self.node_index = node_index
        self.nodes = nodes
        print(graph)
        # BFS
        res = []
        self.res = []
        for i in range(len(nodes)):
            visited = set([i])
            self.dfs(i, visited, [nodes[i]])
        return self.res
    
    def dfs(self, ind, visited, path):
        if len(path) == len(self.nodes):
            self.res = [i for i in path]
            return 
        next_nodes = self.graph[ind]
        for next_ in next_nodes:
            next_id = self.node_index[next_]
            if next_id in visited:
                continue
            visited.add(next_id)
            path.append(self.nodes[next_id])
            self.dfs(next_id, visited, path)
            path.pop()
            visited.remove(next_id)
    
if __name__ == "__main__":
    print(Solution().findSeq(sample_input))
        
        

            




