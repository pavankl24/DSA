from collections import defaultdict, deque

class Solution(object):
    def maximumDetonation(self, bombs):
        n = len(bombs)
        adj = defaultdict(list)
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    adj[i].append(j)
        
        def bfs(start_node):
            queue = deque([start_node])
            visited = {start_node}
            
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)
        
        max_bombs = 0
        for i in range(n):
            max_bombs = max(max_bombs, bfs(i))
            
        return max_bombs
