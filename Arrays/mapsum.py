class MapSum(object):

    def __init__(self):
        self.map = {}
        self.root = {}

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        
        curr = self.root
        for char in key:
            if char not in curr:
                curr[char] = {'sum': 0}
            curr = curr[char]
            curr['sum'] += delta

    def sum(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr:
                return 0
            curr = curr[char]
        return curr['sum']
