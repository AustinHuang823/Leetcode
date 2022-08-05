from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, p = [], sorted(p)
        for i in range(len(s)-len(p)+1):
            if sorted(s[i:i+len(p)]) == p: ans.append(i)
        return ans
    
    
class Solution2: # time limit exceeded
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        originP = p
        for i in range(len(s)-len(p)+1):
            p = originP
            if s[i] in p:
                for j in range(len(p)):
                    if s[i+j] in p:
                        p = p.replace(s[i+j],'',1)
                    else: break
                if len(p) == 0: ans.append(i)
        # s = s.replace('a','',1)
        return ans
        
if __name__ == '__main__':
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(sol.findAnagrams(s, p))