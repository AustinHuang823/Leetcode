from typing import Optional, List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            res = max((r - l) * min(height[l], height[r]), res)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return res

        
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    print(sol.maxArea(height))