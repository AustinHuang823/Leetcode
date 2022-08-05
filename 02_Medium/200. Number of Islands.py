from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        Land = []
        
        def dfs(i,j):
            if 0 <= i < r and 0<= j < c and grid[i][j] == "1":
                grid[i][j] = 0
                return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
            return 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    Land.append(dfs(i,j))
                
        return len(Land)
            
            
class Solution2:
    def numIslands(self, grid):
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
        
if __name__ == '__main__':
    sol = Solution2()
    grid = [  ["1","1","0","0","0"],  ["1","1","0","0","0"],  ["0","0","1","0","0"],  ["0","0","0","1","1"]]
    print(sol.numIslands(grid))