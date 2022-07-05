from platform import node
from typing import List
from unittest import result

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def arr2TreeNode(arr) -> TreeNode:
    nodeArr = [TreeNode]
    for n in arr:
        if n is not None:
            nodeArr.append(TreeNode(n))
        else:
            nodeArr.append(None)
    for i in range(1, len(nodeArr)):
        if nodeArr[i]:
            if 2 * i < len(nodeArr):
                nodeArr[i].left = nodeArr[2 * i]
            if 2 * i + 1 < len(nodeArr):
                nodeArr[i].right = nodeArr[2 * i + 1]
    return nodeArr[1]

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, par = None):
            
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.res += 1
                    covered.update({node, par, node.left, node.right})

        self.res = 0
        covered = {None}
        dfs(root)
        return self.res
        
class Solution2:
    # Here is our greedy solution:
    # Set cameras on all leaves' parents, thenremove all covered nodes.
    # Repeat step 1 until all nodes are covered.


    # Apply a recusion function dfs.
    # Return 0 if it's a leaf.
    # Return 1 if it's a parent of a leaf, with a camera on this node.
    # Return 2 if it's coverd, without a camera on this node.

    # For each node,
    # if it has a child, which is leaf (node 0), then it needs camera.
    # if it has a child, which is the parent of a leaf (node 1), then it's covered.

    # If it needs camera, then res++ and we return 1.
    # If it's covered, we return 2.
    # Otherwise, we return 0.
    def minCameraCover(self, root):
        self.res = 0
        def dfs(root):
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.res

class Solution3:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if node is None:
                return 'covered'
            l, r = dfs(node.left), dfs(node.right)
            if l==r=='covered':
                return 'to_be_covered'
            if l=='to_be_covered' or r=='to_be_covered':
                self.res += 1
                return 'covering'
            if l=='covering' or r=='covering':
                return 'covered'
        # if dfs(root) == 'to_be covered':
            # self.res += 1
        return (dfs(ansTN)=='to_be_covered') + self.res
        # return self.res

class Solution4:
    def minCameraCover(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(node):
            if node is None:
                return 'covered'
            l, r = dfs(node.left), dfs(node.right)
            if l==r=='covered':
                return 'to_be_covered'
            if l=='to_be_covered' or r=='to_be_covered':
                self.result += 1
                return 'covering'
            if l=='covering' or r=='covering':
                return 'covered'
        print(self.result)
        return (dfs(ansTN)== 'to_be_covered') + self.result

if __name__ == '__main__':
    sol = Solution4()
    root = [0,0,None,0,None,0,None,None,0]
    ansTN = arr2TreeNode(root)
    print(sol.minCameraCover(ansTN))