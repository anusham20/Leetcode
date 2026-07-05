import heapq
class Solution:

    def feasibility(self, graph: Dict[Dict[List[int]]], online: List[bool], value: int, k: int) -> bool:
        # applies BFS to find a path based on the value that ensures the edges are greater than it but less than k
        maxCost = 0
        cost, starting_node = (0, 0)
        queue = [(cost, starting_node)]
        n = len(online) # this is the number of nodes
        best_cost = {0 : 0}
        visited = set()
        
        while len(queue) > 0:
            cost_from_u, u = heapq.heappop(queue)
            endpoints = graph.get(u, {})

            if u in visited:
                continue
            visited.add(u)

            for v, elist in endpoints.items():
                for e in elist:
                    
                    if e < value: # if edge cost is less than value, it is not useful enough
                        continue
                    if v != n - 1 and not online[v]: # passes if node is not online
                        continue

                    new_cost = cost_from_u + e
                    if new_cost > k: # still too expensive
                        continue
                    
                    if v == n - 1: # end state
                        return True

                    if v not in best_cost or new_cost < best_cost[v]:
                        heapq.heappush(queue, (new_cost, v))
                        best_cost[v] = new_cost
        return False

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph = {}
        for i in range(len(edges)):
            u, v, e = edges[i]
            if u not in graph:
                graph[u] = {}
            if v not in graph[u]:
                graph[u][v] = []
            graph[u][v].append(e)
            # we have to use a list to store the edge cost as what if there are the same edge but different cost
        
        # Binary Search
        low = 0
        high = max(e for _, _, e in edges) if edges else 0 # largest edge weight

        # applies binary search to find the optimal score 
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            if self.feasibility(graph, online, mid, k):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer