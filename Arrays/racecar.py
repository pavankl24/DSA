class Solution(object):
    def racecar(self, target):
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            k = i.bit_length()
            if i == (1 << k) - 1:
                dp[i] = k
                continue
            dp[i] = dp[(1 << k) - 1 - i] + k + 1
            for j in range(k - 1):
                dp[i] = min(dp[i], dp[i - (1 << (k - 1)) + (1 << j)] + k - 1 + j + 2)
        return dp[target]
