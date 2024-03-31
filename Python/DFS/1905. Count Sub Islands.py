from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid2[i][j] == 0:
                return None
            
            grid2[i][j] = 0
            for a, b in [0,1], [0,-1], [1,0], [-1,0]:
                dfs(i+a, j+b)
        
        for i1 in range(m):
            for j1 in range(n):
                if grid2[i1][j1] == 1 and grid1[i1][j1] == 0:
                    dfs(i1, j1)     
        
        count = 0
        for i2 in range(m):
            for j2 in range(n):
                if grid2[i2][j2] == 1:
                    dfs(i2, j2)
                    count += 1
        
        return count

        
if __name__ == '__main__':
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    sol = Solution()
    print(sol.countSubIslands(grid1, grid2))