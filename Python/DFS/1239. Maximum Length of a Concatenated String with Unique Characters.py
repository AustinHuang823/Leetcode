from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.res = 0
        
        def dfs(input, path, pos):
            if pos > len(arr):
                return
            temp_path = ""
            for c in input:
                if c in path or c in temp_path:
                    return
                temp_path += c
            
            path += input
            self.res = max(self.res, len(path))
            for i in range(pos, len(arr)):
                dfs(arr[i], path, i+1)
                    
        for i in range(len(arr)):            
            dfs(arr[i], "", i+1)
        
        return self.res

        
if __name__ == "__main__":
    arr = ["abc", "d", "de", "def"]
    sol = Solution()
    print(sol.maxLength(arr))