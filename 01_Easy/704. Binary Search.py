from statistics import median
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        The idea is using a pivot in our binary search
        once the nums[pivot] > target, remove the integers behind the nums -----(1)
        and if nums[pivot] < target, remove the integers in front of nums -----(2)
        and if nums[pivot] == target, we return the position of our pivot
            since the length of nums varies when we operate our function
            we would need a variable(here I use pos) to store the numbers as we remove indexs from nums, 
            which at the same time is the value of pivot -----(3)
        """        
        pos = 0 #-----(3)
        while nums: #once there's no index left in nums, we jump out of the loop
            pivot = len(nums) // 2
            if nums[pivot] > target: #-----(1)
                nums = nums[:pivot]
            elif nums[pivot] < target: #-----(2)
                nums = nums[pivot+1:]
                pos += pivot+1 #-----(3)
            elif nums[pivot] == target:
                pos += pivot #-----(3)
                return pos
        return -1
        
if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(sol.search(nums,target))        
        