class SolutionT:
    def removeDuplicates(self, s: str) -> str:
        dupe = True
        while dupe:
            if not s: return ""
            dupe = False
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s = s[:i] + s[i+2:]
                    dupe = True
                    break
        return s

import collections
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = list(s)
        while s:
            stack.append(s.pop())
            while stack and s and stack[-1] == s[-1]:
                stack = stack[:-1]
                s = s[:-1]


        return "".join(stack[::-1])

if __name__ == "__main__":
    s = "cbbcca"
    sol = Solution()
    print(sol.removeDuplicates(s))