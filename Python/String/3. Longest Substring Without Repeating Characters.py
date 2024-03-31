class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        n = len(s)
        
        if n == 0:
            return 0
        
        for l in range(n):
            memo = []
            for r in range(l, n):
                if s[r] not in memo:
                    memo.append(s[r])
                else:
                    break
            res = max(res, len(memo))
        return res
        
if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))