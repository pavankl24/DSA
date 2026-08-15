class Solution(object):
    def longestSubsequence(self, nums):
        total_xor = 0
        has_nonzero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        if total_xor != 0:
            return len(nums)
            
        return len(nums) - 1 if has_nonzero else 0
