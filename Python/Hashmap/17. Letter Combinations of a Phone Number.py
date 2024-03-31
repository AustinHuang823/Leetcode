from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {"2":"abc", "3": "def","4": "ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8": "tuv", "9": "wxyz"}
        stack = []
        res = []
        for n in digits:
            if n in map:
                if len(res) == 0:
                    for k in range(len(map[n])):
                        stack.append(map[n][k])
                else:
                    for m in res:
                        for k in range(len(map[n])):
                            stack.append(m + map[n][k])
                res = stack
                stack = []
                        
        return res

if __name__ == '__main__':
    digits = "23"
    sol = Solution()
    print(sol.letterCombinations(digits))