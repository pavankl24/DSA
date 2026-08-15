class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = list(triangle[-1])
        
        for row in range(n - 2, -1, -1):
            for i in range(row + 1):
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
                
        return dp[0]
