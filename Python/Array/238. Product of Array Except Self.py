from typing import List

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = nums.count(0)
        if zero_cnt > 1: return [0]*len(nums)
        
        product = 1
        for n in nums:
            if n != 0:
                product = product * n
        for i, c in enumerate(nums):
            if zero_cnt:
                if c == 0: nums[i] = product
                else: nums[i] = 0
            else:
                nums[i] = product // c
        return nums
        

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_from_left, product_from_right = 1, 1
        len_nums = len(nums)
        res = [1] * len_nums
        for i in range(len_nums-1):
            product_from_left *= nums[i]
            res[i+1] *= product_from_left

        for i in range(len_nums-1, 0, -1):
            product_from_right *= nums[i]
            res[i-1] *= product_from_right
        
        return res
        
if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))