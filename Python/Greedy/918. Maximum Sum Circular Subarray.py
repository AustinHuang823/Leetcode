from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currSum, maxSum = 0, float('-inf')
        sums = sum(nums)
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        
        currSum = 0
        max2 = 0
        for i in range(len(nums)):
            maxSum = max(maxSum, sums+max2)
            sums -= nums[i]
            currSum += nums[i]
            max2 = max(max2, currSum)
        
        return maxSum

if __name__ == '__main__':
    nums = [5,-3,-3,-3,5]
    sol = Solution()
    print(sol.maxSubarraySumCircular(nums))