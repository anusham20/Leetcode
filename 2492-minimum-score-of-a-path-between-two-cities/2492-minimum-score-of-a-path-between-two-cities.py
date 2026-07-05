class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for a, b, d in roads:
            graph[a] = graph.get(a, {})
            graph[a][b] = d
            graph[b] = graph.get(b, {})
            graph[b][a] = d

        visited = set()
        stack = [1]
        best = 10001

        while (len(stack) != 0):
            a = stack.pop()
            if a not in visited:
                visited.add(a)
                neighbors = graph[a]
                for b, d in neighbors.items():
                    best = min(best, d)
                    stack.append(b)
        
        return best