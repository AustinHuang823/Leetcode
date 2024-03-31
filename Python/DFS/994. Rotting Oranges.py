from typing import List
import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def Rotting(i, j): # function to make oranges rotten
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 2

        count = 0
        prev = copy.deepcopy(grid) # use deepcopy here to prevent prev from changing when modifying grid
        while self.iffresh(grid): # if there's fresh orange in grid then start process of rotting
            for n in range(len(grid)):
                for m in range(len(grid[0])):
                    if prev[n][m] == 2: # when current orange is rotten, make its neighbor rotting
                        for (a,b) in [(1,0),(0,1),(-1,0),(0,-1)]:
                            Rotting(n+a,m+b)
            count += 1 # when the whole grid get rotten, we count for 1 time

            # if there is fresh orange in grid(which is be detected by the while line)
            # but the grid isn't different from prev, mean there are unrottable oranges, return -1
            if prev == grid:
                return -1
            else:
                prev = copy.deepcopy(grid) # memory current grid for next round comparison
        return count

    
    def iffresh(self, grid): # function to detect if there's any fresh orange in grid
        for row in grid:
            for n in row:
                if n == 1: return True
        return False



if __name__ == '__main__':
    grid = [[1],[2]]
    sol = Solution()
    print(sol.orangesRotting(grid))