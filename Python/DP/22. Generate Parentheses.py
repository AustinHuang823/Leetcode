from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.helper(0,0,n,"")
        return self.result

    def helper(self, open, close, n, current):
        if len(current) == 2*n:
            self.result.append(current)
            return
        
        if open < n and open >= close:
            self.helper(open+1, close, n, current+"(")
        if close < n and open >= close:
            self.helper(open, close+1, n, current+")")
