from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        reserved_rows = defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_rows[row] |= (1 << (seat - 2))
        
        max_groups = (n - len(reserved_rows)) * 2
        
        left_mask = 0b00001111   
        middle_mask = 0b00111100 
        right_mask = 0b11110000   
        
        for mask in reserved_rows.values():
            cnt = 0
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            
            if left_free:
                cnt += 1
            if right_free:
                cnt += 1
                
            if not left_free and not right_free:
                if (mask & middle_mask) == 0:
                    cnt += 1
                    
            max_groups += cnt
            
        return max_groups
