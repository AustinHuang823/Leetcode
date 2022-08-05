class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for _ in range(maxMove):
            # deep copy of dp
            t = [s[:] for s in dp] #[:]clone the ele in []
            for x in range(m):
                for y in range(n):
                    a = t[x-1][y] if x > 0 else 1
                    b = t[x+1][y] if x + 1 < m else 1
                    c = t[x][y-1] if y > 0 else 1
                    d = t[x][y+1] if y + 1 < n else 1
                    dp[x][y] = a + b + c + d
        return dp[startRow][startColumn] % (10**9+7)
    
    
class Solutio2:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        global pathscount
        pathscount = 0
        def dfs(i,j,move):
            #move out of bound
            if i < 0 or i >= m or j < 0 or j >= n and move <= maxMove:
                global pathscount
                pathscount += 1
                return
            
            #moving in the bound
            elif 0 <= i < m and 0 <= j < n and move < maxMove:
                dfs(i-1,j,move+1)
                dfs(i+1,j,move+1) 
                dfs(i,j-1,move+1)
                dfs(i,j+1,move+1)
                
        dfs(startRow,startColumn,0)
        return pathscount % (10**9 + 7)
        
        
        
        
if __name__ == '__main__':
    m = 2 #rows
    n = 2 #cols
    maxMove = 2
    startRow = 0
    startColumn = 0
    sol = Solution()
    print(sol.findPaths(m,n,maxMove,startRow,startColumn))