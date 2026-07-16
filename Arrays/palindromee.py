class Solution(object):
    def palindromePairs(self, words):
        word_to_index = {word: i for i, word in enumerate(words)}
        pairs = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                if prefix == prefix[::-1]:
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_index and word_to_index[reversed_suffix] != i:
                        pairs.append([word_to_index[reversed_suffix], i])

                if j < n and suffix == suffix[::-1]:
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_index and word_to_index[reversed_prefix] != i:
                        pairs.append([i, word_to_index[reversed_prefix]])

        return pairs
