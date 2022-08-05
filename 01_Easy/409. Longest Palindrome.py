
from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        cs = ''  #character storage
        sc = [0 for _ in range(n)]  #storage counter
        for i in range(n):
            if s[i] not in cs:
                cs = "".join((cs,s[i]))
                sc[cs.index(s[i])] += 1
            else: 
                sc[cs.index(s[i])] += 1
        
        OL = 0 #output length 
        for j in range(n):
            while sc[j] >= 2 :
                sc[j] -= 2
                OL += 2
                
        return OL + (sum(sc) > 0)
            

class Solution2:
    def longestPalindrome(self, s: str) -> int:
            D = {}
            for c in s:
                if c in D:
                    D[c] += 1
                else:
                    D[c] = 1
            print(D)
            L = D.values()
            print(L)
            E = len([i for i in L if i % 2 == 1])
            print(E)
            return sum(L) - E + (E > 0)

if __name__ == '__main__': 
    sol = Solution()
    s = "abccccdd"
    print(sol.longestPalindrome(s))