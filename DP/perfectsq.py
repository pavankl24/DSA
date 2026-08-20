class Solution:
    def numSquares(self, n):
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        
        if int(n**0.5)**2 == n:
            return 1
            
        for i in range(1, int(n**0.5) + 1):
            if int((n - i*i)**0.5)**2 == n - i*i:
                return 2
                
        return 3
