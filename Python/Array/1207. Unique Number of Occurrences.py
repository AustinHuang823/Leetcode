from typing import List
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        OccuranceCount = collections.Counter(arr)
        stack = []
        for F in OccuranceCount.values():
            if F not in stack:
                stack.append(F)
            else:
                return False
        return True

if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    sol = Solution()
    print(sol.uniqueOccurrences(arr))