from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        
        
        if not len(matrix) or not len(matrix[0]):
            # Quick response for empty matrix
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        for row in matrix:
			
			# range check
            if row[0] <= target <= row[-1]:
                
				# launch binary search on current possible row
				
                left, right = 0, w-1
                
                while left <= right:
                    
                    mid = left + (right - left) // 2
                    
                    mid_value = row[mid]
                    
                    if target > mid_value:
                        left = mid+1
                    elif target < mid_value:
                        right = mid-1
                    else:
                        return True
                
        return False

class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:

        
        if not len(matrix) or not len(matrix[0]):
			# Quick response for empty matrix
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        # Start adaptive search from bottom left corner
        y, x = h-1, 0
        
        while True:
            
            if y < 0 or x >= w:
                break
            
            current = matrix[y][x]
            
            if target < current:
                # target is smaller, then go up
                y -= 1
            
            elif target > current:
                # target is larger, then go right
                x += 1
            
            else:
                # hit target
                return True
            
        return False

class Solution2: # time limit exceeded
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return bool(self.dfs(0, 0, target, matrix, {}))
    
    def dfs(self, r, c, target, matrix, dp):
        if r > len(matrix) - 1 or c > len(matrix[0]) - 1 or matrix[r][c] > target: return 0 
        if matrix[r][c] == target: return 1
        if (r, c) in dp: return dp[(r,c)]
        
        if r <= len(matrix) - 1 and c <= len(matrix[0]) - 1 and matrix[r][c] < target: 
            return max(self.dfs(r + 1, c, target, matrix, dp), self.dfs(r, c+1, target, matrix, dp))
        
        
        
        
if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    sol = Solution()
    print(sol.searchMatrix(matrix, target))