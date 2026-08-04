class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i - 1 - limit >= 0:
                    dp[i][j][0] = (dp[i][j][0] - dp[i-1-limit][j][1] + MOD) % MOD
                
                dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j - 1 - limit >= 0:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j-1-limit][0] + MOD) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
