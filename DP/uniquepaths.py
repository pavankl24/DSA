import math

class Solution(object):
    def uniquePaths(self, m, n):
        return math.comb(m + n - 2, m - 1)
