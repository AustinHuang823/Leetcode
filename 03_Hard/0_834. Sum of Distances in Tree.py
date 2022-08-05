from typing import List
import collections

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        # Explanation
        # Let's solve it with node 0 as root.

        # Initial an array of hashset tree, tree[i] contains all connected nodes to i.
        # Initial an array count, count[i] counts all nodes in the subtree i.
        # Initial an array of res, res[i] counts sum of distance in subtree i.

        # Post order dfs traversal, update count and res:
        # count[root] = sum(count[i]) + 1
        # res[root] = sum(res[i]) + sum(count[i])

        # Pre order dfs traversal, update res:
        # When we move our root from parent to its child i, count[i] points get 1 closer to root, n - count[i] nodes get 1 futhur to root.
        # res[i] = res[root] - count[i] + N - count[i]

        # return res, done.
        
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res
        
        

if __name__ == '__main__':
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    sol = Solution()
    print(sol.sumOfDistancesInTree(n,edges))