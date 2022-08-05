from typing import List
import heapq

class Solution2:
    def lastStoneWeight(self, A):
        h = [-x for x in A]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        
        while stones: #here we remove all the 0 weight stones in list
            if stones[0] == 0:
                stones.remove(0)
            else: break # for the cases that len(stones) == 0 and stones[0] != 1, break to next step
            
        if len(stones) == 0: #cases that the result is 0
            return 0
        elif len(stones) == 1: #cases that only 1 stone remains
            return stones[0]
        else: # here's the main lines to conduct what the problem demands.
            maxstone, secstone = stones[-1], stones[-2]
            stones[-1] = maxstone - secstone
            stones[-2] = 0
        
        return self.lastStoneWeight(stones) #iter here so we will keep conduct our lines to the result we want 
        
if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    sol = Solution2()
    print(sol.lastStoneWeight(stones))