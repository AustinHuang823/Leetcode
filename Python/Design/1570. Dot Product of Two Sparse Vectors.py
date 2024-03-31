from typing import List
import collections
class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec):
        # Return the dotProduct of two sparse vectors
        res = 0
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                res += n * vec.nonzeros[i]
        return res
        
        

# Your SparseVector object will be instantiated and called as such:
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print(ans)