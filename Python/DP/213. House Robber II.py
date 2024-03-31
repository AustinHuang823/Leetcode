class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums)
        
        dp = [nums[0], nums[1], nums[0]+nums[2]]
        for i in range(3, len(nums)-1):
            dp[0], dp[1], dp[2] = max(dp[0], dp[1]), max(dp[1], dp[2]), max(dp[0]+nums[i], dp[1]+nums[i])
        
        res = max(dp)
        dp = [nums[1], nums[2], nums[1]+nums[3]]
        for i in range(4, len(nums)):
            dp[0], dp[1], dp[2] = max(dp[0], dp[1]), max(dp[1], dp[2]), max(dp[0]+nums[i], dp[1]+nums[i])

        res = max(res, max(dp))
        return res
        
