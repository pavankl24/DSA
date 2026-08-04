class Solution(object):
    def findMissingElements(self, nums):
        num_set = set(nums)
        return [x for x in range(min(nums), max(nums) + 1) if x not in num_set]
