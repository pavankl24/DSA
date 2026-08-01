from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, level + 1))
        return 0
