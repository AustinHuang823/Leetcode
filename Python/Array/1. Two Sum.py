from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for l in range(n):
            for r in range(n-1, l, -1):
                if nums[l] + nums[r] == target:
                    return [l, r]
        
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums,target))