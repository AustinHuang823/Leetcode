from typing import Optional
from typing import List
import collections
import DS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return
        dic = {}
        res = set()
        nodes = collections.deque([root])
        while nodes:
            node = nodes.popleft()
            if node.val not in dic:
                dic[node.val] = [node]
            else:
                for n in dic[node.val]:
                    if self.sametree(n, node):
                        res.add(n)
                        break
                else:
                    dic[node.val].append(node)
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return list(res)

            


    def sametree(self, root1, root2):
        if root1.val != root2.val:
            return False
        tree1, tree2 = collections.deque([root1]), collections.deque([root2])

        while tree1 and tree2:
            r1, r2 = tree1.popleft(), tree2.popleft()
            if r1.val != r2.val:
                return False

            if r1.left and r2.left:
                tree1.append(r1.left)
                tree2.append(r2.left)
            elif r1.left or r2.left:
                return False

            if r1.right and r2.right:
                tree1.append(r1.right)
                tree2.append(r2.right)
            elif r1.right or r2.right:
                return False
        return True
        


if __name__ == '__main__':
    root = DS.arr2TreeNode([1,2,3,4,None,2,4,None,None,4])
    sol = Solution()
    print(sol.findDuplicateSubtrees(root))