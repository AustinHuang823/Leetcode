from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = []
        for n in arr:
            temp.append(abs(n - x))
        
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if temp[l] > temp[r]:
                l += 1
            else:
                r -= 1
        
        return arr[l:r + 1]
            

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = -1
    sol = Solution()
    print(sol.findClosestElements(arr, k, x))