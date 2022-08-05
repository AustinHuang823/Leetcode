from lib2to3.pgen2.pgen import DFAState
from typing import List

class Solution: #Optimization of Sol4
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums[1:len(nums)])
        for i in range(len(nums)+1):
            if i == len(nums):
                return -1
            if l == r:
                return i
            l += nums[i]
            if i+1 <= len(nums)-1:
                r -= nums[i+1]

class Solution4:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i == len(nums):
                return -1
            if sum(nums[0:i]) == sum(nums[i+1:len(nums)]):
                return i
            

class Solution3: # since nums[i] may be negative, binary search doesn't work here
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        i = (l + r + 1) // 2
        return self.BS(0, len(nums)-1, i, nums)
    
    def BS(self, l, r, i, nums):#binary BS
        if sum(nums[0:i]) == sum(nums[i+1 : len(nums)+1]):        
            return i
        if l == r or l > r and sum(nums[0:i]) != sum(nums[i+1 : len(nums)+1]):
            return -1
        
        if sum(nums[0:i]) < sum(nums[i+1 : len(nums)+1]):
            r = i
            i = (l + r) // 2
            return self.BS(l, r, i, nums)
        elif sum(nums[0:i]) > sum(nums[i+1 : len(nums)+1]):
            l = i
            i = (l + r + 1) // 2
            return self.BS(l, r, i, nums)
            

class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        l,r = 0,0
        for i in range(len(nums)):
            l = sum(nums[0:i])
            r = sum(nums[i+1:len(nums)+1])
            
            if l == r :return i
            
            elif l !=r and i == len(nums)-1:
                i=-1
        
        return i
                

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.pivotIndex(nums))        
        