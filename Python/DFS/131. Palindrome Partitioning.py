from typing import List
import collections

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        lst = []
        def palindrome(a):
            return a == a[::-1]
        def dfs(i,curr):
            if i == len(s):
                lst.append(curr)
                return 
            for j in range(i,len(s)):
                sol = s[i:j+1]
                if palindrome(sol):
                    dfs(j+1, curr + [sol])
            return 
        dfs(0,[])
        return lst

if __name__ == '__main__':
    s = "aab"
    sol = Solution()
    print(sol.partition(s))