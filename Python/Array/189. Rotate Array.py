from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)

        k = k%L
        nums.reverse()

        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        
        for i in range((L-k)//2):
            nums[k+i], nums[-i-1] = nums[-i-1], nums[k+i]

        return nums
    

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol = Solution()
    print(sol.rotate(nums, k))