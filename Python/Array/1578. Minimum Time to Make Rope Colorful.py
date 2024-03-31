from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                res += min(neededTime[i], neededTime[i+1])
                neededTime[i+1] = max(neededTime[i], neededTime[i+1])
        return res


class Solution1:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        i = 0
        while i < len(colors)-1:
            if colors[i] == colors[i+1]:
                colors = colors[:i] + colors[i+1:]
                if neededTime[i] < neededTime[i+1]:
                    res += neededTime[i]
                    neededTime = neededTime[:i] + neededTime[i+1:]
                else:
                    res += neededTime[i+1]
                    neededTime = neededTime[:i+1] + neededTime[i+2:]
            else:
                i += 1
        return res
            

if __name__ == '__main__':
    colors = "aabaa"
    neededTime = [1,2,3,4,1]
    sol = Solution()
    print(sol.minCost(colors, neededTime))