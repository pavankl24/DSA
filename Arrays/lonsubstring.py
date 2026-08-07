class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        max_len = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            seen[char] = i
            max_len = max(max_len, i - start + 1)
            
        return max_len
