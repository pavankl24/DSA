class Solution(object):
    def alternateDigitSum(self, n):
        s = str(n)
        return sum(int(d) if i % 2 == 0 else -int(d) for i, d in enumerate(s))
