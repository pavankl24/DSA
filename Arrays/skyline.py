import heapq


class Solution(object):

    def getSkyline(self, buildings):
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result = [[0, 0]]
        max_heap = [(0, float("inf"))]

        for x, negated_height, right in events:
            if negated_height != 0:
                heapq.heappush(max_heap, (negated_height, right))

            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)

            current_max_height = -max_heap[0][0]

            if result[-1][1] != current_max_height:
                result.append([x, current_max_height])

        return result[1:]
