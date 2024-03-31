from typing import List
import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        hasApple[0], degree = True, [0] * n
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        queue = collections.deque(v for v in range(n) if degree[v] == 1)
        while queue:
            u = queue.popleft()
            if hasApple[u]: continue
            for v in graph[u]:
                if degree[v] > 0:
                    degree[v] -= 1
                    degree[u] -= 1
                    if degree[v] == 1:
                        queue.append(v)
        return sum(degree)

if __name__ == '__main__':
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,True,True,False]
    sol = Solution()
    print(sol.minTime(n, edges, hasApple))