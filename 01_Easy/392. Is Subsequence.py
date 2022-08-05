from typing import List

class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        a= list(t)
        b= list(s)
        if t == s:
            return True
        for i in range(len(a)-1, -1, -1):
            if a[i] not in s:
                a.remove(a[i])
            if a == b:
                return True
        return False    

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
        # remainder_of_t = iter(t)
        
        # for letter in s:
        #     if letter not in remainder_of_t:
        #         return False
        # return True


if __name__ == '__main__': #vscode main line
    sol = Solution()
    s = "acb"
    t = "ahbgdc"
    print(sol.isSubsequence(s,t))