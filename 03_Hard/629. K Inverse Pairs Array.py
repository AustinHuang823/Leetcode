class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        max_possible_inversions = (n * (n-1)//2)
        if k > max_possible_inversions:
            return 0
        if k == 0 or k == max_possible_inversions:
            return 1
        
        MOD = pow(10,9) + 7
        
        dp = [[0]*(k+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][0] = 1

        dp[2][1] = 1
        
        for i in range(3,n+1):
            max_possible_inversions = min(k, i*(i-1)//2)
            for j in range(1,  max_possible_inversions + 1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] 
                if j>=i:
                    dp[i][j] -= dp[i-1][j - i]
                dp[i][j] = (dp[i][j] + MOD) % MOD
            
        return dp[n][k]

class Solution2:
    # f(n,k) = sum(f(n-1,i)), where max(k-n+1,0) <= i <= k
    # f(0,k) = 0
    # f(n,0) = 1
        
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            
            for j in range(1, k + 1): 
                dp[j] += dp[j - 1]
                
            for j in range(k, 0, -1): 
                dp[j] -= j - i >= 0 and dp[j - i]
                
        return dp[k] % (10**9 + 7)
        
        
if __name__ == '__main__':
    n = 3
    k = 1
    sol = Solution()
    print(sol.kInversePairs(n,k))