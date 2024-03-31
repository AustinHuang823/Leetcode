from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        #dfs line
        def dfs(i, j, memo):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != start:
                return
            
            if (i,j) in memo:
                return
            else:
                if image[i][j] == start:
                    image[i][j] = color
                    
            memo[(i,j)] = 1
            dfs(i + 1, j, memo)
            dfs(i - 1, j, memo)
            dfs(i, j + 1, memo)
            dfs(i, j - 1, memo)
        
        if start != color:
            dfs(sr, sc, {})
        
        return image
        

        
        
if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    sol = Solution()
    print(sol.floodFill(image, sr, sc, color))