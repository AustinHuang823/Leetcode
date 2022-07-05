from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
       horizontalCuts.sort()
       verticalCuts.sort()
       
       Max_h = 0
       for idxh in range(len(horizontalCuts)-1):
          if Max_h < horizontalCuts[idxh+1] - horizontalCuts[idxh]:
              Max_h = horizontalCuts[idxh+1] - horizontalCuts[idxh]
              
       if  horizontalCuts[0] > Max_h: Max_h = horizontalCuts[0]
       if  h - horizontalCuts[-1] > Max_h: Max_h = h-horizontalCuts[-1]
       
       Max_w = 0
       for idxw in range(len(verticalCuts)-1):
          if Max_w < verticalCuts[idxw+1] - verticalCuts[idxw]:
              Max_w = verticalCuts[idxw+1] - verticalCuts[idxw]
              
       if  verticalCuts[0] > Max_w: Max_w = verticalCuts[0]
       if  w - verticalCuts[-1] > Max_w: Max_w = w-verticalCuts[-1]
       
       return Max_h * Max_w % ((10 ** 9)+7)
       
        
        
if __name__ == '__main__':
    h = 5
    w = 4
    horizontalCuts = [3,1]
    verticalCuts = [1]
    sol = Solution()
    print(sol.maxArea(h,w,horizontalCuts,verticalCuts))