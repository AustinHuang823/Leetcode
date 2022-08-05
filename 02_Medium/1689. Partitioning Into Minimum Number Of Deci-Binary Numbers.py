from typing import List

class Solution:
    def minPartitions(self, n: str) -> int:
        TempArr = [int(a) for a in n]
        # print(TempArr)
        return max(TempArr)
        
class Solution2:
    def minPartitions(self, n: str) -> int:
        # print(max(n))
        # return int(max(n))
        print(n)
        return max(n)

class Solution3:
    def minPartitions(self, n: str) -> int:
        ans = float('-inf')
        for i in range(len(n)):
            if int(n[i]) > ans:
                ans = int(n[i])
        return ans
    
    
if __name__ == '__main__':
    n = "82734"
    sol = Solution3()
    print(sol.minPartitions(n))
