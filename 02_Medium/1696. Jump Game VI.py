from typing import List
class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(n):
            maxV = float('-inf')
            for j in range(i-k, i):
                if j>=0:
                    maxV = max(maxV, dp[j])
            if maxV == float("-inf"):
                maxV = 0
            dp[i] = nums[i] + maxV
        return dp[n-1]
    
import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
#         Better Approach: Using Priority Queue (Max Heap): T = O(N x log k); S = O(k) 
# Idea: Searching the DP array for max value in previous 'k' elements takes Time = O(k). 
# Is there a better way to get the max value in previous 'k' elements? Yes, using a max-heap we can retreive the priority queue in O(1) time 
# but we need to adjust the priority queue again such that the next maximum element is at the top and this takes O(log k) time.
        n = len(nums)
        queue = []
        val = 0
        for i in range(n):
            maxV = 0
            if queue:
                maxV, indx = queue[0]
                while indx+k < i:
                    maxV, indx = heapq.heappop(queue)
                heapq.heappush(queue, [maxV,indx])
            val = nums[i] + (-1) * maxV
            heapq.heappush(queue, [-1 * val, i]) 
        return val
        
# Now problem with python, there is nothing called max-heap in python, the "heapq" is a min-heap by default.
# So to use this min-heap as a max-heap, we multiply the value by -1 such that the smallest element becomes the largest and the largest element becomes the smallest.
# And whenever we want to get the actual value we multiply -1 again to the value in the min-heap.

# The min-heap may contain values that are not in a distance of previous 'k' from 'i'. So we keep deleting the values whose index in nums is not in a range of 'k' from 'i' by using the while indx+k < i:  loop inside.

        
        
if __name__ == '__main__':
    nums = [1,-1,-2,4,-7,3]
    k = 2
    sol = Solution()
    print(sol.maxResult(nums,k))
