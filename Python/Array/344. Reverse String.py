from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        count = 0
        while count < n//2:
            s[count], s[n-count-1] = s[n-count-1], s[count] 
            count += 1
        return s

if __name__ == '__main__':
    s = ["h","e","l","a","o","a"]
    sol = Solution()
    print(sol.reverseString(s))