class Solution(object):
    def findMaximumScore(self, nums):
        ans = 0
        ma = 0
        for i in range(len(nums) - 1):
            ma = max(ma, nums[i])
            ans += ma
        return ans
