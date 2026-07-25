from collections import Counter

class Solution(object):
    def countPairs(self, deliciousness):
        ans = 0
        MOD = 10**9 + 7
        count = Counter()
        powers = [1 << i for i in range(22)]
        
        for x in deliciousness:
            for p in powers:
                if p - x in count:
                    ans = (ans + count[p - x]) % MOD
            count[x] += 1
            
        return ans
