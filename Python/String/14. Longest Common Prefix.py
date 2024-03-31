from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        eq = True
        i = 0
        while eq and i < len(strs[0]):
            cur = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != cur:
                    eq = False
                    break
            if eq:
                res += cur
                i += 1
        return res


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))