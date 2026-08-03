class Solution(object):
    def minFlips(self, s):
        n = len(s)
        s = s + s
        
        target1 = "".join("0" if i % 2 == 0 else "1" for i in range(2 * n))
        target2 = "".join("1" if i % 2 == 0 else "0" for i in range(2 * n))
        
        diff1 = 0
        diff2 = 0
        ans = float('inf')
        
        for i in range(2 * n):
            if s[i] != target1[i]:
                diff1 += 1
            if s[i] != target2[i]:
                diff2 += 1
                
            if i >= n:
                if s[i - n] != target1[i - n]:
                    diff1 -= 1
                if s[i - n] != target2[i - n]:
                    diff2 -= 1
                    
            if i >= n - 1:
                ans = min(ans, diff1, diff2)
                
        return ans
