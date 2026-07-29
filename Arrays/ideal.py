from collections import Counter

class Solution(object):
    def idealArrays(self, n, maxValue):
        MOD = 10**9 + 7
        
        max_k = min(n, 15)
        fact = [1] * (n + max_k + 1)
        inv = [1] * (n + max_k + 1)
        for i in range(1, len(fact)):
            fact[i] = (fact[i-1] * i) % MOD
        inv[-1] = pow(fact[-1], MOD - 2, MOD)
        for i in range(len(fact) - 2, -1, -1):
            inv[i] = (inv[i+1] * (i + 1)) % MOD
            
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv[r] % MOD * inv[n-r] % MOD

        ans = 0
        for i in range(1, maxValue + 1):
            temp = i
            p_counts = []
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    c = 0
                    while temp % d == 0:
                        c += 1
                        temp //= d
                    p_counts.append(c)
                d += 1
            if temp > 1:
                p_counts.append(1)
                
            ways = 1
            for c in p_counts:
                ways = (ways * nCr(n + c - 1, c)) % MOD
            ans = (ans + ways) % MOD
            
        return ans
