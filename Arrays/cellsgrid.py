from collections import defaultdict

class Solution(object):
    def maxScore(self, grid):
        val_to_rows = defaultdict(int)
        for r, row in enumerate(grid):
            for val in row:
                val_to_rows[val] |= (1 << r)
                
        unique_vals = sorted(val_to_rows.keys())
        num_vals = len(unique_vals)
        memo = {}
        
        def dp(idx, mask):
            if idx == num_vals:
                return 0
            if (idx, mask) in memo:
                return memo[(idx, mask)]
                
            res = dp(idx + 1, mask)
            val = unique_vals[idx]
            
            rows_with_val = val_to_rows[val]
            temp = rows_with_val
            while temp > 0:
                lsb = temp & -temp
                row_idx = lsb.bit_length() - 1
                if not (mask & lsb):
                    score = val + dp(idx + 1, mask | lsb)
                    if score > res:
                        res = score
                temp &= temp - 1
                
            memo[(idx, mask)] = res
            return res
            
        return dp(0, 0)
