class Solution(object):
    def checkAdjacent(self, (r, c), (m, n)):
        return 0 <= r < m and 0 <= c < n
    
    def atEndState(self, (r, c), (m, n)):
        return r == m - 1 and c == n - 1

    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        grid_length = len(grid)
        grid_height = len(grid[0])

        starting_health = health - grid[0][0]
        if starting_health <= 0: return False

        queue = [(0, 0, starting_health)]

        best = [[0 for _ in range(grid_height)] for _ in range(grid_length)]
        best[0][0] = starting_health

        while len(queue) > 0:
            r_curr, c_curr, health_curr = queue.pop(0)
            if self.atEndState((r_curr, c_curr), (grid_length, grid_height)):
                return True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r_curr, dc + c_curr

                if self.checkAdjacent((nr, nc), (grid_length, grid_height)):
                    new_health = health_curr - grid[nr][nc]
                    if new_health > 0 and new_health > best[nr][nc]:
                        best[nr][nc] = new_health
                        queue.append((nr, nc, new_health))
        return False
