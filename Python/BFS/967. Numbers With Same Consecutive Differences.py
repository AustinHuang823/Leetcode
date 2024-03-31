from typing import List
import collections

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        queue = collections.deque([])
        temp_queue = collections.deque([])
        for i in range(1, 10):
            queue.append(i)
        
        n -= 1
        while n:
            n -= 1
            while queue:
                cur_n = queue.popleft()
                cur_n_last = cur_n % 10
                if cur_n_last - k >= 0 :
                    temp_queue.append(cur_n*10 + cur_n_last-k)
                if cur_n_last + k < 10:
                    temp_queue.append(cur_n*10 + cur_n_last+k)
            queue = temp_queue.copy()
            temp_queue = collections.deque([])

        return sorted(list(set(queue)))

if __name__ == '__main__':
    n = 2
    k = 0
    sol = Solution()
    print(sol.numsSameConsecDiff(n,k))