from typing import List
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in range(n): # i is column start
            for j in range(i, n): # j is column end
                counter = collections.defaultdict(int)
                cur, counter[0] = 0, 1
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += counter[cur - target]
                    counter[cur] += 1
        return res

    
if __name__ == '__main__':
    matrix = [[0,1,0],[1,1,1],[0,1,0]]
    target = 0
    sol = Solution()
    print(sol.numSubmatrixSumTarget(matrix,target))