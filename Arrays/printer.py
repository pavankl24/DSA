class Solution(object):
    def strangePrinter(self, s):
        if not s:
            return 0
            
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j - 1] + 1
                
                for k in range(i, j):
                    turns = dp[i][k] + dp[k + 1][j]
                    if s[k] == s[j]:
                        turns -= 1
                    dp[i][j] = min(dp[i][j], turns)
                    
        return dp[0][n - 1]
