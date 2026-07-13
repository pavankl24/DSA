import random

class Solution(object):

    def __init__(self, n, blacklist):
        self.blacklist = set(blacklist)
        self.m = n - len(self.blacklist)
        self.mapping = {}
        
        last = n - 1
        for b in self.blacklist:
            if b < self.m:
                while last in self.blacklist:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self):
        idx = random.randint(0, self.m - 1)
        return self.mapping.get(idx, idx)
