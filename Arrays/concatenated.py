class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        memo = {}

        def canForm(word):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set or canForm(suffix):
                        memo[word] = True
                        return True
            
            memo[word] = False
            return False

        res = []
        for word in words:
            if canForm(word):
                res.append(word)
        return res
