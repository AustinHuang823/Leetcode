from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        here the problem ask for logn complexity, hence we prepare to conduct a binary search here
        """
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        # quick test for empty nums and nums that don't contain target
        
        l, r = 0, len(nums) - 1
        while nums[l] < target or nums[r] > target:
            if l == r - 1 and nums[l] != target and nums[r] != target: return [-1,-1] #cases that nums don't contain target
            if nums[(l + r) // 2] < target: l = (l + r) // 2 + int(bool(r - l == 1))
            elif nums[(l + r) // 2] > target: r = (l + r) // 2 
            elif nums[(l + r) // 2] == target: l, r = (r - l) // 4 + int(bool((r - l) % 4))+ l, r - (r - l) // 4 - int(bool((r - l) % 4))
        # here we conduct a binary search. after the operation, l, r will both be the index which nums[index] == target
        
        while l - 1 >= 0 and nums[l - 1] == target:
            l -= 1
        while r + 1 <= len(nums) - 1 and nums[r + 1] == target:
            r += 1
        # move both l, r to the edge of continuous target
        
        return [l,r]
    
        
if __name__ == '__main__':
    nums = [0,0,1,2,3,3,4]
    target = 2
    sol = Solution()
    print(sol.searchRange(nums,target))