from typing import List
import collections

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = sorted(collections.Counter(nums).items(), key = lambda x: -x[1])
        res = []
        for i in range(k):
            res.append(dic[i][0])
            
        return res
    
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] -= 1
            else:
                dic[i] = -1
        
        h = []
        
        for key in dic:
            heapq.heappush(h, (dic[key], key))
        print(h)
        res = []
        for i in range(k):
            val, target = heapq.heappop(h)
            print(val, target)
            res.append(target)
            
        return res
    
if __name__ == '__main__':
    nums = [5,3,1,1,1,3,73,1]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))