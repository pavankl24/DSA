class Solution(object):
    def largestNumber(self, nums):
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0

        num_strs = map(str, nums)
        num_strs.sort(cmp=compare)
        
        result = "".join(num_strs)
        return "0" if result[0] == "0" else result
