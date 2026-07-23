class Solution(object):
    def arrayNesting(self, nums):
        max_length = 0
        
        for i in range(len(nums)):
            if nums[i] != -1:
                start = nums[i]
                count = 0
                curr = i
                
                while nums[curr] != -1:
                    temp = nums[curr]
                    nums[curr] = -1  
                    curr = temp      
                    count += 1
                
                max_length = max(max_length, count)
                
        return max_length
