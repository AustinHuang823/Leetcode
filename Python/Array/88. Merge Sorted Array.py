from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r1, r2 = m-1, n-1
        r = m+n-1
        while r >= 0:
            if r1 < 0:
                nums1[r] = nums2[r2]
                r2 -= 1
            elif r2 < 0:
                nums1[r] = nums1[r1]
                r1 -= 1
            elif nums1[r1] >= nums2[r2]:
                nums1[r] = nums1[r1]
                r1 -= 1
            else:
                nums1[r] = nums2[r2]
                r2 -= 1
            r -= 1
        print(nums1)


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [4,5,6]
    n = 3
    sol = Solution()
    print(sol.merge(nums1, m, nums2, n))