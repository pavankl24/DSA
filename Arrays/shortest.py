class Solution(object):
    def shortestBridge(self, grid):
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def get_first_island():
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        return r, c

        start_r, start_c = get_first_island()
        queue = [(start_r, start_c)]
        island1 = [(start_r, start_c)]
        grid[start_r][start_c] = -1
        
        ptr = 0
        while ptr < len(island1):
            r, c = island1[ptr]
            ptr += 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = -1
                    island1.append((nr, nc))
                    
        queue = island1
        distance = 0
        
        while queue:
            next_queue = []
            for r, c in queue:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return distance
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1
                            next_queue.append((nr, nc))
            queue = next_queue
            distance += 1
            
        return distance
