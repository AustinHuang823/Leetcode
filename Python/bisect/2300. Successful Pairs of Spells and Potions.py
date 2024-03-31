from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        N = len(potions)
        res = []

        for n in spells:
            if success % n:
                atleast = success//n + 1
            else:
                atleast = success//n
            
            l, r = 0, N
            while l < r:
                mid = (l+r) // 2
                if potions[mid] < atleast:
                    l = mid + 1
                else:
                    r = mid
            res.append(N-l)

        return res


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
sol = Solution()
print(sol.successfulPairs(spells, potions, success))