class Solution(object):
    def removeBoxes(self, boxes):
        memo = {}
        
        def calculatePoints(l, r, k):
            if l > r:
                return 0
            
            if (l, r, k) in memo:
                return memo[(l, r, k)]
            
            original_l, original_k = l, k
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1
                
            res = (k + 1) * (k + 1) + calculatePoints(l + 1, r, 0)
            
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l]:
                    points_by_merging = calculatePoints(l + 1, m - 1, 0) + calculatePoints(m, r, k + 1)
                    res = max(res, points_by_merging)
                    
            memo[(original_l, r, original_k)] = res
            return res
            
        return calculatePoints(0, len(boxes) - 1, 0)
