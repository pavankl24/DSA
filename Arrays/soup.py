class Solution(object):
    def soupServings(self, n):
        if n >= 4800:
            return 1.0
            
        scaled_n = (n + 24) // 25
        memo = {}
        
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
                
            if (a, b) in memo:
                return memo[(a, b)]
                
            prob = 0.25 * (
                dfs(a - 4, b) + 
                dfs(a - 3, b - 1) + 
                dfs(a - 2, b - 2) + 
                dfs(a - 1, b - 3)
            )
            
            memo[(a, b)] = prob
            return prob
            
        return dfs(scaled_n, scaled_n)
