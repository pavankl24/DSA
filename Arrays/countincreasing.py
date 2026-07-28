class Solution(object):
    def countQuadruplets(self, nums):
        n = len(nums)
        ans = 0
        count = [0] * n
        
        for l in range(n):
            less = 0
            for s in range(l):
                if nums[s] < nums[l]:
                    ans += count[s]
                    less += 1
                elif nums[s] > nums[l]:
                    count[s] += less
                    
        return ans
