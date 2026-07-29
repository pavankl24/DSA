class Solution(object):
    def findChampion(self, grid):
        n = len(grid)
        for team in range(n):
            is_champion = True
            for other_team in range(n):
                if team != other_team and grid[other_team][team] == 1:
                    is_champion = False
                    break
            if is_champion:
                return team
