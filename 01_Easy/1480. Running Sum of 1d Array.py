from typing import List 

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums),1):
            nums[i] = nums[i-1] + nums[i]
        return nums
        
if __name__ == '__main__': 
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.runningSum(nums))