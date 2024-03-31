from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = []
        n = len(nums)
        for i in range(n):
            PrevMap.append(target - nums[i])
        for j in range(n):
            if nums[j] in PrevMap and j != PrevMap.index(nums[j]):
                return [j, PrevMap.index(nums[j])]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {}

        for i,n in enumerate(nums):
            Diff = target - n
            if Diff in PrevMap:
                return [PrevMap[Diff],i]
            PrevMap[n]=i
            
        
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums,target))