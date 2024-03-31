import collections
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        m, visited, queue = {}, set(), collections.deque([node])
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(node.val)
            for neighbor in n.neighbors:
                if neighbor not in m:
                    m[neighbor] = Node(neighbor.val)
                m[n].neighbors.append(m[neighbor])
                queue.append(neighbor)
        return m[node]

if __name__ == '__main__':
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    sol = Solution()
    print(sol.cloneGraph(adjList))
