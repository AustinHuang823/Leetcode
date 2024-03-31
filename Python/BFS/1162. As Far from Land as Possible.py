import copy
import collections
from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        qu = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    qu.append([i,j])

        if len(qu)==0 or len(qu)==len(grid)*len(grid[0]):
            return -1

        level = 0
        while len(qu)!=0:
            for i in range(len(qu)):
                i,j = qu.popleft()
                if i>0 and grid[i-1][j]==0:
                    qu.append([i-1,j])
                    grid[i-1][j]=1
                if i<len(grid)-1 and grid[i+1][j]==0:
                    qu.append([i+1,j])
                    grid[i+1][j]=1
                if j>0 and grid[i][j-1]==0:
                    qu.append([i,j-1])
                    grid[i][j-1]=1
                if j<len(grid[0])-1 and grid[i][j+1]==0:
                    qu.append([i,j+1])
                    grid[i][j+1]=1
            level+=1
        
        return level-1

class Solution2:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # check if there's still land to grow
        def landcheck(grid):
            check = set()
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] not in check:
                        check.add(grid[i][j])
            if len(check) == 2:
                return True
            return False
        # function to grow land
        def landgrow(grid):
            tempgrid = copy.deepcopy(grid)
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if tempgrid[i][j] == 1:
                        for d in directions:
                            if 0<= i + d[0] < len(grid) and 0 <= j + d[1] < len(grid[0]):
                                grid[i+d[0]][j+d[1]] = 1

        count = 0
        while landcheck(grid):
            count += 1
            landgrow(grid)

        return count if count else -1

if __name__ == '__main__':
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    sol = Solution()
    print(sol.maxDistance(grid))