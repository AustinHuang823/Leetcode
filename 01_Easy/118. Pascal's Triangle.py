from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(1,numRows + 1):
            tri.append([1 for _ in range(i)])
                   
        for n in range(1,len(tri)):
            for m in range(1,n):
                tri[n][m] = tri[n-1][m-1] + tri[n-1][m]
        
        return tri
        
if __name__ == '__main__': 
    sol = Solution()
    numRows = 5
    print(sol.generate(numRows))