from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)
            
        dp = {0: 0}
        
        for ch in key:
            next_dp = {}
            for target in pos[ch]:
                next_dp[target] = float('inf')
                for curr, steps in dp.items():
                    diff = abs(target - curr)
                    min_dist = min(diff, n - diff)
                    next_dp[target] = min(next_dp[target], steps + min_dist)
            dp = next_dp
            
        return min(dp.values()) + len(key)
