from typing import List 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        if nums[0] > target:
            while l < r:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r

                if nums[(l+r)//2] > nums[0] or nums[(l+r)//2] < target:
                    l = (l+r)//2
                else:
                    r = (l+r)//2
                
                if r == l+1 and nums[r] != target and nums[l] != target:
                    return -1
            if nums[l] != target:
                return -1
        else:
            while l < r:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r

                if nums[(l+r)//2] < nums[0] or nums[(l+r)//2] > target:
                    r = (l+r)//2
                else:
                    l = (l+r)//2

                if r == l+1 and nums[r] != target and nums[l] != target:
                    return -1
            if nums[l] != target:
                return -1
        return l

if __name__ == '__main__':
    nums = [1,3,5]
    target = 3
    sol = Solution()
    print(sol.search(nums, target))