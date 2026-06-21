from collections import Counter

class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        for num in sorted(count):
            while count[num] > 0:
                for i in range(num, num + k):
                    if count[i] == 0:
                        return False
                    count[i] -= 1

        return True