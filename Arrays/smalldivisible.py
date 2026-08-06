class Solution(object):
    def smallestNumber(self, n, t):
        curr = n
        while True:
            prod = 1
            for d in str(curr):
                prod *= int(d)
                if prod == 0:
                    break
            if prod % t == 0:
                return curr
            curr += 1
