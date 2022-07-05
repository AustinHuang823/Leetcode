from typing import List

from pip import main
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        Max_N = max(nums)
        Min_N = min(nums)
        TempArr = []
        
        if len(nums)==1:
            return 0
        
        for i in range(Min_N, Max_N+1):
            dn = 0 #dynamic number
            for j in range(len(nums)):
                if i > nums[j]:
                    dn += i - nums[j]
                elif i <= nums[j]:
                    dn += nums[j] - i
            TempArr.append(dn)
        return min(TempArr)

import statistics
class Solution2:
    def minMoves2(self, nums: List[int]) -> int:
        N = statistics.median(nums)
        dp = 0
        for i in range(len(nums)):
            if nums[i]> N:
                dp += nums[i] - N
            elif nums[i] <= N:
                dp += N - nums[i]
        return int(dp)


                    
    
        
if __name__ == '__main__':
    nums =  [1,10,3,9,5]
    sol = Solution2()
    print(sol.minMoves2(nums))