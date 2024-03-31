from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] >= target:
                r = mid

        return l
        

                


if __name__ == '__main__':
    nums = [1,3,5]
    target = 2
    sol = Solution()
    print(sol.searchInsert(nums, target))