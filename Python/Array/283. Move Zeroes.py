from typing import List 

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        
        def move(nums, pos):
            #if 0, start checking with nums[-1], nums[-2].... if nums[-?] ~= 0, swap
            
            #once nums[-?] reach pos: break, don't move
            for j in range(len(nums) - 1, pos, -1):
                if nums[j] != 0:
                    nums[j], nums[pos] = nums[pos], nums[j]
                    
        for i in range(len(nums)):
            if nums[i] == 0:
                move(nums, i)
                
        return nums
    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        end = len(nums) - 1
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
        
        
if __name__ == '__main__':
    nums = [0,1,0,3,12]
    sol = Solution1()
    print(sol.moveZeroes(nums))