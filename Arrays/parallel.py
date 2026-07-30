from collections import deque


class Solution(object):

    def minimumTime(self, n, relations, time):
        graph = [[] for _ in range(n + 1)]
        in_degree = [0] * (n + 1)

        for u, v in relations:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque()
        max_time = [0] * (n + 1)

        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)
                max_time[i] = time[i - 1]

        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                max_time[neighbor] = max(
                    max_time[neighbor], max_time[curr] + time[neighbor - 1]
                )
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return max(max_time)
