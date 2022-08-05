from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c  = len(grid), len(grid[0])
        maximum = 0
        
        def dfs(i,j):
            if 0 <= i < r and 0 <= j < c and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            else: # means grid[i][j] == 0 or out of bound
               return 0

                
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    maximum = max(dfs(i,j),maximum)

              
        return maximum
        
        
                    
        
        
        
        
if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))


