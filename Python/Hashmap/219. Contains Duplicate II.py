from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


class Solution1_TLE:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for r in range(1, k+1):
            l = 0
            while r < len(nums):
                if nums[l] == nums[r]:
                    return True
                l, r = l+1, r+1
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))