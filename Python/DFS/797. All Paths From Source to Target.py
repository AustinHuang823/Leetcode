from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1

        res = []
        def dfs(pos, curPath):
            if pos == target:
                res.append(curPath.copy())
                return
            
            for n in graph[pos]:
                dfs(n, curPath+[n])
        
        dfs(0,[0])

        return res



if __name__ == '__main__':
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    sol = Solution()
    print(sol.allPathsSourceTarget(graph))