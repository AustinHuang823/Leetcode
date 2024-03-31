from typing import List
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = collections.Counter(p)
        i = 0
        while i < len(p):
            if s[i] in dic:
                dic[s[i]] -= 1
            i += 1
        
        res = []
        if self.ifall0(dic.values()):
            res.append(0)
        
        while i < len(s):
            if s[i] in dic:
                dic[s[i]] -= 1
            if s[i-len(p)] in dic:
                dic[s[i-len(p)]] += 1
            i+=1

            if self.ifall0(dic.values()):
                res.append(i-len(p))
        
        return res


    def ifall0(self, dic_val):
        for n in dic_val:
            if n != 0:
                return False
        return True


class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        all_alpha = "abcdefghijklmnopqrstuvwxyz"
        dic = {}
        for c in all_alpha:
            dic[c] = 0

        for cp in p:
            dic[cp] += 1
        
        for cs in s[:len(p)]:
            dic[cs] -= 1

        res = []
        if self.ifall0(dic.values()):
            res.append(0)

        for i in range(len(p),len(s)):
            dic[s[i]] -= 1
            dic[s[i-len(p)]] += 1
            if self.ifall0(dic.values()):
                res.append(i-len(p)+1)
        
        return res
        

    def ifall0(self, dic_val):
        for n in dic_val:
            if n != 0:
                return False
        return True


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    sol = Solution()
    print(sol.findAnagrams(s, p))
