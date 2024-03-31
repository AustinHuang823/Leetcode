class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CharSet = []
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in CharSet: #meaning it's a duplicate
                CharSet.remove(s[l])
                l += 1
            CharSet.append(s[r])
            res = max(res, r - l + 1)
        return res
        
if __name__ == '__main__':
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))