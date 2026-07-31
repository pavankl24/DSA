class Solution(object):
    def minStartingIndex(self, s, pattern):
        def get_z(string):
            n = len(string)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and string[z[i]] == string[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z

        m = len(pattern)
        n = len(s)
        
        z1 = get_z(pattern + s)
        z2 = get_z(pattern[::-1] + s[::-1])
        
        for i in range(n - m + 1):
            prefix_match = z1[m + i]
            suffix_match = z2[m + (n - m - i)]
            if prefix_match + suffix_match >= m - 1:
                return i
                
        return -1
