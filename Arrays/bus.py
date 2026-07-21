from collections import defaultdict, deque

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
            
        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)
                
        queue = deque([(source, 0)])
        visited_stops = {source}
        visited_buses = set()
        
        while queue:
            stop, bus_count = queue.popleft()
            
            for bus_id in stop_to_buses[stop]:
                if bus_id in visited_buses:
                    continue
                visited_buses.add(bus_id)
                
                for next_stop in routes[bus_id]:
                    if next_stop == target:
                        return bus_count + 1
                        
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, bus_count + 1))
                        
        return -1
