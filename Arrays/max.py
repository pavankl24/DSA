import heapq

class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        min_heap = []
        speed_sum = 0
        max_perf = 0
        
        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)
            speed_sum += spd
            
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
                
            max_perf = max(max_perf, speed_sum * eff)
            
        return max_perf % (10**9 + 7)
