class Solution(object):
    def fallingSquares(self, positions):
   
        intervals = []
        ans = []
        current_max = 0
        
        for left, side in positions:
            right = left + side
            base_height = 0
            
            for l, r, h in intervals:
                if left < r and right > l:
                    base_height = max(base_height, h)
            
            new_height = base_height + side
            intervals.append((left, right, new_height))
            
            current_max = max(current_max, new_height)
            ans.append(current_max)
            
        return ans
