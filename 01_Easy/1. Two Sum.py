from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #for l in range(len(nums)):
        #    for r in range(len(nums)):# and l<r:
        #        if nums[l] + nums[r] == target and l!=r:
        #            return l,r
        # print(target//2)
        PrevMap = {}

        for i,n in enumerate(nums):
            Diff = target - n
            if Diff in PrevMap:
                return [PrevMap[Diff],i]
            PrevMap[n]=i
        # #return

        
                
if __name__ == '__main__':
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    print(sol.twoSum(nums,target))