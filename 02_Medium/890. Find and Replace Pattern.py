import collections
from typing import List
import collections

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if not pattern or not words:
            return None
        res = []
        for word in words:
            if self.isPattern(word, pattern) == True:
                res.append(word)
        return res
        
        
    def isPattern(self, word, pattern):
        for i in range(len(word)):
            par = collections.Counter(pattern[:i+1])
            compare = collections.Counter(word[:i+1])
            if list(par.values()) != list(compare.values()):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    words = ["badc","abab","dddd","dede","yyxx"]
    pattern = "baba"
    print(sol.findAndReplacePattern(words, pattern))