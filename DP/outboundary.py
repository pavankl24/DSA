class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        
        total_paths = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for _ in range(maxMove):
            next_dp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                                total_paths = (total_paths + dp[r][c]) % MOD
                            else:
                                next_dp[nr][nc] = (next_dp[nr][nc] + dp[r][c]) % MOD
            dp = next_dp
            
        return total_paths
