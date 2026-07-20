class Solution(object):
    def xorOperation(self, n, start):
        ans = 0
        for i in range(n):
            ans ^= (start + 2 * i)
        return ans
