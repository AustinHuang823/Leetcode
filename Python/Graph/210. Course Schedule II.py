from typing import List
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for course, prereq in prerequisites:
            if prereq not in graph:
                graph[prereq] = [course]
            else:
                graph[prereq].append(course)

        # # Step 1: Build the graph
        # graph = collections.defaultdict(list)
        # for course, prereq in prerequisites:
        #     graph[prereq].append(course)
        # Step 2: Calculate the in-degree of each node
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            in_degree[course] += 1
        
        # Step 3: Perform topological sort
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            if node in graph:
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
        
        # Step 4: Check for cycle
        if len(result) < numCourses:
            return []
        
        return result

if __name__ == '__main__':
    # numCourses = 3
    # prerequisites = [[1,0],[2,0],[0,2]]
    # prerequisites = [[0,1],[0,2],[1,2]]
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    sol = Solution()
    print(sol.findOrder(numCourses,prerequisites))