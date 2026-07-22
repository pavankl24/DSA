class Solution(object):
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == 1:
                return float(prefix[n] - prefix[i]) / (n - i)
            
            res = 0.0
            for m in range(i + 1, n - j + 2):
                val = float(prefix[m] - prefix[i]) / (m - i) + dp(m, j - 1)
                if val > res:
                    res = val
                    
            memo[(i, j)] = res
            return res
            
        return dp(0, k)
