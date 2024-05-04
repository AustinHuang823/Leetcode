from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums, left, right):
            if left >= right:
                return
            pivot = nums[left + (right - left) // 2]
            l, r = left, right
            while l <= r:
                while nums[l] < pivot:
                    l += 1
                while nums[r] > pivot:
                    r -= 1
                
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            quickSort(nums, left, r)
            quickSort(nums, l, right)
            
        quickSort(nums, 0, len(nums) - 1)
        return nums