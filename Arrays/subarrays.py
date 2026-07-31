class Solution(object):
    def countCompleteSubarrays(self, nums):
        total_distinct = len(set(nums))
        ans = 0
        left = 0
        counts = {}
        for right in range(len(nums)):
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            while len(counts) == total_distinct:
                ans += len(nums) - right
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1
        return ans
