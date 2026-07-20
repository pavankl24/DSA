import heapq

class Solution(object):
    def smallestRange(self, nums):
        min_heap = []
        current_max = float('-inf')
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])
            
        ans_start, ans_end = float('-inf'), float('inf')
        
        while min_heap:
            current_min, list_idx, element_idx = heapq.heappop(min_heap)
            
            if current_max - current_min < ans_end - ans_start:
                ans_start, ans_end = current_min, current_max
                
            if element_idx + 1 == len(nums[list_idx]):
                break
                
            next_val = nums[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
            current_max = max(current_max, next_val)
            
        return [ans_start, ans_end]
