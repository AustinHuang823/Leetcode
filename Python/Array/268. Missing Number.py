from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_n, max_n = min(nums), max(nums)
        for n in range(len(nums)):
            if n + min_n not in nums:
                return n
        return max_n + 1
if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    print(sol.missingNumber(nums))