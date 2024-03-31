from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        
        # dfs function
        def dfs(i ,j, memo):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]):
                return
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            return min 
        
if __name__ == '__main__':
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    sol = Solution()
    print(sol.minimumEffortPath(heights))