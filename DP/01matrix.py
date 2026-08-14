class Solution(object):
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        inf = m + n
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] != 0:
                    top = mat[r-1][c] if r > 0 else inf
                    left = mat[r][c-1] if c > 0 else inf
                    mat[r][c] = 1 + min(top, left)
                    
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] != 0:
                    bottom = mat[r+1][c] if r < m - 1 else inf
                    right = mat[r][c+1] if c < n - 1 else inf
                    mat[r][c] = min(mat[r][c], 1 + min(bottom, right))
                    
        return mat
