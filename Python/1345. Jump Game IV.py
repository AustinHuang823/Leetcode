from typing import List
import collections

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = {}
        for i in range(len(arr)):
            if arr[i] not in graph:
                graph[arr[i]] = []
            if i+1 < len(arr) and arr[i] == arr[i+1] and i-1 >= 0 and arr[i] == arr[i-1]:
                continue
            graph[arr[i]].append(i)

        dq = collections.deque([(0, 0)])
        visited = {0: 0}
        while dq:
            pos, steps = dq.popleft()
            if pos == len(arr)-1:
                return steps
            if pos-1 > 0:
                if pos-1 not in visited:
                    visited[pos-1] = steps+1
                    dq.append((pos-1, steps+1))
                else:
                    if steps+1 < visited[pos-1]:
                        visited[pos-1] = steps+1
                        dq.append((pos-1, steps+1))
            if pos+1 < len(arr):
                if pos+1 not in visited:
                    visited[pos+1] = steps+1
                    dq.append((pos+1, steps+1))
                else:
                    if steps+1 < visited[pos+1]:
                        visited[pos+1] = steps+1
                        dq.append((pos+1, steps+1))
            for i in graph[arr[pos]]:
                if i != pos:
                    if i not in visited:
                        visited[i] = steps+1
                        dq.append((i, steps+1))
                    else:
                        if steps+1 < visited[i]:
                            visited[i] = steps+1
                            dq.append((i, steps+1))
        return -1


        


if __name__ == '__main__':
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    sol = Solution()
    print(sol.minJumps(arr))