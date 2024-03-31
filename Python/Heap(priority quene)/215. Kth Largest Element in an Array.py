from typing import List
import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         #new empty list
#         hq = []
#         heapq.heapify(hq)
#         # use heap, push pop(nums) into hq
#         for n in nums:
#             heapq.heappush(hq, n)
        
        
#         return hq
#         #while loop, count loop times < k, pop out hq elements
        
#         #return hq[0]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for item in nums:
            if len(heap) < k or item >= heap[0]:
                heapq.heappush(heap, item)
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]
    
if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 2
    sol = Solution()
    print(sol.findKthLargest(nums, k))