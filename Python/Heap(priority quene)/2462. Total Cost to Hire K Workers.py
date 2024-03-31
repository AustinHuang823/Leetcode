from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = costs[:candidates]
        qq = costs[max(candidates, len(costs)-candidates):]
        print(qq)
        heapq.heapify(q)
        heapq.heapify(qq)

        i = candidates
        ii = len(costs) - candidates - 1
        ans = 0
        for _ in range(k):
            if not qq or q and q[0]<= qq[0]:
                ans += heapq.heappop(q)
                if i <= ii:
                    heapq.heappush(q, costs[i])
                    i += 1
            else:
                ans += heapq.heappop(qq)
                if i <= ii:
                    heapq.heappush(qq, costs[ii])
                    ii -= 1

        return ans

if __name__ == '__main__':
    costs = [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75]
    k = 13
    candidates = 23
    sol = Solution()
    print(sol.totalCost(costs, k, candidates))