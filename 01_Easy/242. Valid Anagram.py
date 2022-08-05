class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s, t_s= sorted(list(s)), sorted(list(t))
        if s_s == t_s:
            return True
        return False
        
if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s,t))