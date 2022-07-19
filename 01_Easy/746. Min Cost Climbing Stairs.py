from typing import List
import timeit

start = timeit.default_timer()

class Solution2: # Passed Solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}
        
        def dfs(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = min(dfs(i+1) + cost[i], dfs(i+2) + cost[i])
            return dp[i]
        
        stop = timeit.default_timer()
        print('Passed Solution time: ', stop - start)  
        
        return min(dfs(0), dfs(1))

class Solution: # My time limit exceeded solution
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i < len(cost):
                return min(dfs(i+1) + cost[i], dfs(i+2) + cost[i])
            if i >= len(cost):
                return 0

        stop = timeit.default_timer()
        print('My time limt exceeded solution time: ', stop - start)
        
        return min(dfs(0), dfs(1))
            
        
if __name__ == '__main__': #vscode main line
    sol = Solution2()
    cost = [841,462,566,398,243,248,238,650,989,576,361,126,334,729,446,897,456,487,145,156,123]
    print(sol.minCostClimbingStairs(cost))
