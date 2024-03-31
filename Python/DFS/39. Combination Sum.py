from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        temp = []
        def dfs(cursum, path):
            if cursum > target:
                return
            elif cursum == target:
                temp.append(path)
            for i in candidates:
                dfs(cursum + i, path+[i])
        
        dfs(0, [])
        res = []
        for l in temp:
            if sorted(l) not in res:
                res.append(sorted(l))

        return res

class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(cursum, index, path):
            if cursum > target:
                return
            elif cursum == target:
                res.append(path)
            for i in range(index, len(candidates)):
                dfs(cursum + candidates[i], i, path+[candidates[i]])
        
        dfs(0, 0, [])

        return res

if __name__ == '__main__':
    candidates = [2,3,6,7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates, target))
