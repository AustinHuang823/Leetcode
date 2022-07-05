from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        
        for c in range(N+1):
            dp[0][c] = c
        
        for r in range(M+1):
            dp[r][0] = r
        
        for r in range (1, M+1):
            for c in range(1,N+1):
                if word1[c-1] == word2[r-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1])
                    
        return dp[-1][-1]               
        



if __name__ == "__main__":
    sol = Solution()
    test_1 = ( "sea", "eat", 2) #(input, expected result)
    test_2 = ( "leetcode", "etco", 4)
    tests = (test_1, test_2)
    for idx, (test_case, expected_result) in enumerate(tests):
        result = sol.minDistance(test_case)
        print(result)
        if result == expected_result:
            print(f"test {idx + 1} passed")
        else:
            print(f"test {idx + 1} failed")