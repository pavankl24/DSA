class Solution(object):
    def maxStability(self, n, edges, k):
        def find(i, parent):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i], parent)
            return parent[i]

        def union(i, j, parent):
            root_i = find(i, parent)
            root_j = find(j, parent)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        parent = list(range(n))
        must_min = float('inf')
        has_must = False
        
        for u, v, s, must in edges:
            if must == 1:
                has_must = True
                must_min = min(must_min, s)
                if not union(u, v, parent):
                    return -1

        parent_all = list(range(n))
        components_all = n
        max_val = 0
        for u, v, s, _ in edges:
            if s > max_val:
                max_val = s
            if union(u, v, parent_all):
                components_all -= 1
                
        if components_all > 1:
            return -1

        def can_form(target):
            if has_must and target > must_min:
                return False
            
            parent_test = list(range(n))
            components_test = n
            
            for u, v, s, must in edges:
                if must == 1:
                    union(u, v, parent_test)
                    components_test -= 1
                    
            upgradable = []
            for u, v, s, must in edges:
                if must == 0:
                    if s >= target:
                        if union(u, v, parent_test):
                            components_test -= 1
                    elif s * 2 >= target:
                        upgradable.append((u, v))
                        
            upgrades_used = 0
            for u, v in upgradable:
                if components_test == 1:
                    break
                if union(u, v, parent_test):
                    components_test -= 1
                    upgrades_used += 1
                    if upgrades_used > k:
                        return False
                        
            return components_test == 1

        low = 0
        high = max_val * 2
        if has_must:
            high = min(high, must_min)
            
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if can_form(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
