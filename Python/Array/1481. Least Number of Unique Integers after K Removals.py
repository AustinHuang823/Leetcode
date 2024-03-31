from typing import List
import collections
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr = collections.Counter(arr)
        
        freq = sorted(arr.values())
        ans = len(freq)
        for i in range(len(freq)):
            k -= freq[i]
            if k < 0:
                break
            ans -= 1
        
        return ans
    
class Solution2:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr = collections.Counter(arr)
        hq = []
        for n in arr:
            hq.append((arr[n], n))
        heapq.heapify(hq)
        while k > 0:
            count, _ = heapq.heappop(hq)
            k -= count
        
        return len(hq) if k == 0 else len(hq)+1
        



if __name__ == '__main__':
    arr = [4,3,1,1,3,3,2]
    k = 4
    sol = Solution()
    print(sol.findLeastNumOfUniqueInts(arr,k))