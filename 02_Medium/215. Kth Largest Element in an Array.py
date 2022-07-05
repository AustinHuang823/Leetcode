from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return(nums[len(nums)-k])

import random
class Solution2:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]


if __name__ == '__main__':
    nums = [3,2,1,5,6,4] #[3,2,3,1,2,4,5,5,6]
    k = 2 #4
    sol = Solution2()
    print(sol.findKthLargest(nums,k))

