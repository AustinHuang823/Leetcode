import collections
import heapq
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [(-ord(k), v) for k, v in collections.Counter(s).items()] 
        heapq.heapify(pq)
        ans = []
        while pq: 
            k, v = heapq.heappop(pq)
            if ans and ans[-1] == k: 
                if not pq: break 
                kk, vv = heapq.heappop(pq)
                ans.append(kk)
                if vv-1: heapq.heappush(pq, (kk, vv-1))
                heapq.heappush(pq, (k, v))
            else: 
                m = min(v, repeatLimit)
                ans.extend([k]*m)
                if v-m: heapq.heappush(pq, (k, v-m))
        return "".join(chr(-x) for x in ans)

if __name__ == '__main__':
    s = "cczazcc"
    repeatLimit = 3
    sol = Solution()
    print(sol.repeatLimitedString(s, repeatLimit))