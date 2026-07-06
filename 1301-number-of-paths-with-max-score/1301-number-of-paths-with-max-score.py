class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[(-1,0) for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = (0, 1)
        print(dp)

        bestScore = 0
        paths = 0
        startingState = (bestScore, paths)

        MOD = 10**9 + 7

        # I am going from E to S instead
        for i in range(n):
            board[i] = list(board[i])
        
        directions = [(1, 0), (0, 1), (1, 1)]  # from below/right/diag

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue

                best = -1
                ways = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < n and nc < n:
                        score, cnt = dp[nr][nc]
                        if score == -1:
                            continue

                        if score > best:
                            best = score
                            ways = cnt

                        elif score == best:
                            ways = (ways + cnt) % MOD

                if best == -1:
                    dp[r][c] = (-1, 0)

                else:
                    val = 0 if board[r][c] in ('E', 'S') else int(board[r][c])
                    dp[r][c] = (best + val, ways)

        res_score, res_ways = dp[0][0]

        if res_score == -1:
            return [0, 0]
        
        return [res_score, res_ways % MOD]