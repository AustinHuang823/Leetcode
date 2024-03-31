from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ## RC ##
		## APPROACH : BACKTRACKING ##
        
		## TIME COMPLEXITY : O(N^2) ##
		## SPACE COMPLEXITY : O(N^2) ##
        
        result = []

        def backtracking(curr, num):
            if len(curr) >= 2 and curr[-1] < curr[-2]:
                return
            if len(curr) >= 2 and curr[:] not in result:
                result.append(curr[:])
            for i in range(len(num)):
                backtracking(curr + [num[i]], num[i+1:])
        
        backtracking([], nums)
        return result

if __name__ == '__main__':
    nums = [4,6,7,7]
    sol = Solution()
    print(sol.findSubsequences(nums))