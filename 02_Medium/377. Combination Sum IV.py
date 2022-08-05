from typing import List
class Solution:
    # since we can choose different characters from nums, I assume to conduct a decision tree here
    # for decisioin trees, I choose to use dfs here
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        return self.dfs(nums, {}, target)
    # since the(1,1,2), (1,2,1) both counts for a answer, we don't need to sort our path, therefore the dp here I choose to use a dictionary{}
    
    def dfs(self, nums, dp, target):
        if target < 0: return 0
        elif target == 0: return 1
        
        if target in dp: return dp[target]
        
        count = 0
        for n in nums:
            count += self.dfs(nums, dp, target - n)
            if target - n < 0 : break
            
            
        dp[target] = count
        # print(dp)
        return count
            
        
        
    
if __name__ == '__main__':
    nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    target = 10
    sol = Solution()
    print(sol.combinationSum4(nums, target))