class Solution(object):
    def minCut(self, s):
        n = len(s)
        if n <= 1:
            return 0
            
        is_pal = [[False] * n for _ in range(n)]
        cuts = [0] * n
        
        for i in range(n):
            min_cuts = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True
                    if j == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, cuts[j - 1] + 1)
            cuts[i] = min_cuts
            
        return cuts[n - 1]
