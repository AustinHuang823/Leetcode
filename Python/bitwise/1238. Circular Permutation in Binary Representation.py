from typing import List
import collections
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        q = collections.deque()

        for i in range(0,1<<n):
            q.append(i^(i>>1))
            print(i,i>>1,q)

        while(q[0]!=start):
            q.append(q.popleft())
        
        return list(q)

print(8<<10)
if __name__ == '__main__':
    n = 3
    start = 2
    sol = Solution()
    print(sol.circularPermutation(n,start))
