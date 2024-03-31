class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dfs(count, cursum):
            res = 0
            if cursum > target or count > n:
                return 0
            if count == n and cursum != target:
                return 0
            elif count == n and cursum == target:
                return 1
            
            if (count, cursum) in memo:
                return memo[((count, cursum))]
            
            for i in range(1, k+1):
                res += dfs(count+1, cursum+i)
            
            memo[(count, cursum)] = res
            return res
        
        return dfs(0,0) % (10**9+7)
            
            
        
if __name__ == '__main__':
    n = 1
    k = 6
    target = 3
    sol = Solution()
    print(sol.numRollsToTarget(n, k, target))