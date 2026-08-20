class Solution:
    def maxCoins(self, nums):
        vals = [1] + [x for x in nums if x > 0] + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):
            for left in range(0, n - 1 - length):
                right = left + length + 1
                for i in range(left + 1, right):
                    coins = vals[left] * vals[i] * vals[right]
                    total = coins + dp[left][i] + dp[i][right]
                    if total > dp[left][right]:
                        dp[left][right] = total

        return dp[0][n - 1]
