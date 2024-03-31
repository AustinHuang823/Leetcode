import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        # dic = Counter
        dic = collections.Counter(s)
        
        # sort dic, use key = lambda
        dic = sorted(dic.items(), key = lambda x: x[1])
        
        res = ""
        while dic:
            c, val = dic.pop()
            while val >= 1:
                val -= 1
                res += c
        
        return res
        
if __name__ == '__main__':
    s = "aaatree"
    sol = Solution()
    print(sol.frequencySort(s))