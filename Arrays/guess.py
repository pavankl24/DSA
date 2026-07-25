import random

class Solution(object):
    def findSecretWord(self, words, master):
        def getMatches(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        for _ in range(30):
            count = [[0] * 26 for _ in range(6)]
            for w in words:
                for i, c in enumerate(w):
                    count[i][ord(c) - ord('a')] += 1
            
            best_word = max(words, key=lambda w: sum(count[i][ord(c) - ord('a')] for i, c in enumerate(w)))
            
            matches = master.guess(best_word)
            if matches == 6:
                return
            
            words = [w for w in words if getMatches(best_word, w) == matches]
