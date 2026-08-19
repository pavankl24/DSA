

class Solution:
    def diffWaysToCompute(self, expression):
        memo = {}
        
        def compute(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            for i, c in enumerate(expr):
                if c in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if c == '+':
                                res.append(l + r)
                            elif c == '-':
                                res.append(l - r)
                            elif c == '*':
                                res.append(l * r)
            
            if not res:
                res.append(int(expr))
                
            memo[expr] = res
            return res
            
        return compute(expression)
