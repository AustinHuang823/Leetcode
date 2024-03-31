from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = []
        for c in nums:
            if c in stack:
                stack.remove(c)
            else:
                stack.append(c)
        return stack[0]

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    sol = Solution()
    print(sol.singleNumber(nums))