from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            Diff = target - nums[i]
            if Diff in nums and nums.index(Diff) != i:
                return [nums.index(Diff), i]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {}

        for i,n in enumerate(nums):
            Diff = target - n
            if Diff in PrevMap:
                return [PrevMap[Diff],i]
            PrevMap[n]=i

        
                
if __name__ == '__main__':
    sol = Solution2()
    nums = [11,15,2,7]
    target = 9
    print(sol.twoSum(nums,target))