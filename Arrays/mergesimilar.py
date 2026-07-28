from collections import Counter

class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        counts = Counter()
        for v, w in items1 + items2:
            counts[v] += w
        return sorted([[v, w] for v, w in counts.items()])
