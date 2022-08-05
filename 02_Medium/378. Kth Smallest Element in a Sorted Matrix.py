from typing import List
import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = len(matrix[0])
        m = (k - 1) // l
        n = (k % l - 1) if k > 1 else 0
        return matrix[m][n]
        
class Solution2: # bisect
    def kthSmallest(self, matrix, k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            # Calculating mid element of sorted array
            mid = (lo+hi)//2
            # bisect.bisect_right(iterable, element) gives index of first element that is greater than the targeted value.
            # Similarly bisect.bisect_left(iterable, element) gives index of first element that is greater than or equal to the targeted value.
            # In the context, bisect.bisect_right(row, mid) gives the index where first element that would be greater than mid.
            # This bisect.bisect_right(row, mid) is calculated for all the rows of the matrix to get indices of first element in each row which is greater than mid.
            # Summing up these indices would give us the total number of elements that are less than or equal to mid. 
            # If number of such elements less than calculated mid is <k then we reduce the search space by increasing low=mid+1 (because for mid we've seen that number of elements <= mid are <k)
            # If number of elements less than calculated mid is >=k then we reduce the search space by bringing down high=mid
            print(sum(bisect.bisect_right(row,mid) for row in matrix))
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo        

if __name__ == '__main__':
    sol = Solution2()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(sol.kthSmallest(matrix,k))