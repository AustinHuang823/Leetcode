class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        return self.memo(grid, m-1, n-1, {})

    def memo(self, grid, i, j, dp):
        if i < 0 or j < 0: return 0
        if i == 0 or j == 0: return 1
        if (i,j) in dp: return dp[(i,j)]
        dp[(i,j)] = self.memo(grid, i - 1, j, dp) + self.memo(grid, i, j - 1, dp)
        return dp[(i,j)]


class Solution3:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        if m<0 or n<0: return 0
        if m==1 and n==1: return 1
        if (m,n) in memo:
            return memo[(m,n)]
        memo[(m,n)]=self.uniquePaths(m-1,n,memo)+self.uniquePaths(m,n-1,memo)
        print(memo)
        return memo[(m,n)]
    

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        return self.dfs(grid, m-1, n-1, {})
    
    def dfs(self, grid, i, j, dp):
        if i < 0 or j < 0: return 0
        if i == 0 or j == 0: return 1
        if (i,j) in dp: return dp[(i,j)]
        
        dp[(i,j)] = self.dfs(grid, i-1, j, dp) + self.dfs(grid, i, j-1, dp)
        return dp[(i,j)]
        
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(m - 1 , n - 1, {})
    
    def dfs(self, i, j ,dp):
        if i == 0 and j == 0: return 1
        if i < 0 or j < 0 : return 0
        if (i,j) in dp: return dp[(i,j)]
        
        dp[(i,j)] = self.dfs(i - 1, j , dp) + self.dfs(i, j - 1, dp)
        return dp[(i,j)]
        
        
if __name__ == '__main__':
    sol = Solution()
    sol2 = Solution2()
    sol3 = Solution3()
    sol4 = Solution4()
    m = 3
    n = 2
    print(sol.uniquePaths(m,n),sol2.uniquePaths(m,n),sol4.uniquePaths(m,n))