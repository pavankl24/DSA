from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
            
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == target:
                return steps
                
            for i in range(4):
                digit = int(curr[i])
                for move in (-1, 1):
                    next_digit = (digit + move) % 10
                    next_state = curr[:i] + str(next_digit) + curr[i+1:]
                    
                    if next_state not in visited and next_state not in dead:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
                        
        return -1
