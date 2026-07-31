class Solution(object):
    def divisibilityArray(self, word, m):
        res = []
        curr = 0
        for char in word:
            curr = (curr * 10 + int(char)) % m
            res.append(1 if curr == 0 else 0)
        return res
