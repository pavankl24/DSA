import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        busy_servers = []
        
        ans = []
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            curr_time = max(curr_time, j)
            
            if not free_servers and busy_servers[0][0] > curr_time:
                curr_time = busy_servers[0][0]
                
            while busy_servers and busy_servers[0][0] <= curr_time:
                free_t, w, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (w, idx))  
            w, idx = heapq.heappop(free_servers)
            ans.append(idx)
            heapq.heappush(busy_servers, (curr_time + task_time, w, idx))
            
        return ans
