class Solution(object):

    def closestCost(self, baseCosts, toppingCosts, target):
        self.closest = float("inf")

        def dfs(idx, current_cost):
            if abs(current_cost - target) < abs(self.closest - target):
                self.closest = current_cost
            elif abs(current_cost - target) == abs(self.closest - target):
                self.closest = min(self.closest, current_cost)

            if idx == len(toppingCosts) or current_cost >= target:
                return

            for count in range(3):
                dfs(idx + 1, current_cost + toppingCosts[idx]*count)
        for base in baseCosts:
            dfs(0, base)

        return self.closest
