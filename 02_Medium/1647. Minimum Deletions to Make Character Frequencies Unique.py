from typing import List 

class Solution:
    def minDeletions(self, s: str) -> int:
        TempArr_alpha = []
        TempArr_count = []
        for idx, ele1 in enumerate(s):
            if s[idx] not in TempArr_alpha:
                TempArr_alpha.append(s[idx])
                TempArr_count.append(s.count(s[idx]))
                
        TempArr_n_count = []
        times = 0
        for idy in range(len(TempArr_count)):
            while TempArr_count[idy]  in TempArr_n_count and TempArr_count[idy] != 0: 
                TempArr_count[idy] -= 1
                times += 1
            if TempArr_count[idy] not in TempArr_n_count:
                TempArr_n_count.append(TempArr_count[idy])

        return times

import collections
class Solution2:
    def minDeletions(self, s: str) -> int:
        cnt, res, used = collections.Counter(s), 0, set()
        for ch, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res
        
if __name__ == '__main__':
    s = "bbcebab"
    sol = Solution2()
    print(sol.minDeletions(s))