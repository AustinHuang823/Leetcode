from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        
        for row in triangle[:: -1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
                
        return dp[0]
        

if __name__ == "__main__":
    sol = Solution()
    test_1 = ([[2],[3,4],[6,5,7],[4,1,8,3]], 11) #(input, expected result)
    test_2 = ([[-10]], -10)
    tests = (test_1, test_2)
    for idx, (test_case, expected_result) in enumerate(tests):
        result = sol.minimumTotal(test_case)
        print(result)
        if result == expected_result:
            print(f"test {idx + 1} passed")
        else:
            print(f"test {idx + 1} failed")
