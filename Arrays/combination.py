class Solution(object):
    def combinationSum(self, candidates, target):
        results = []

        def backtrack(remain, combo, start_index):
            if remain == 0:
                results.append(list(combo))
                return
            elif remain < 0:
                return

            for i in range(start_index, len(candidates)):
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i)
                combo.pop()

        backtrack(target, [], 0)
        return results
