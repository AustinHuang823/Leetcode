from typing import List
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        num2full = []
        for i in range(len(capacity)):
            num2full.append(capacity[i] - rocks[i])
        num2full.sort()
        
        fullbagcount = 0
        while additionalRocks > 0 and fullbagcount < len(capacity):
           additionalRocks -= num2full[fullbagcount]
           fullbagcount += 1
        
        return fullbagcount if additionalRocks >= 0 else fullbagcount - 1

if __name__ == '__main__':
    capacity = [2,3,4,5]
    rocks = [1,2,4,4]
    additionalRocks = 2
    sol = Solution()
    print(sol.maximumBags(capacity, rocks, additionalRocks))