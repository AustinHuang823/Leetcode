import collections
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        for l in range(min(len(str1),len(str2)), 0,-1):
            if n1 % l == 0 and n2 % l == 0:
                if str1[:l] != str2[:l]:
                    break
                if str1 == str1[:l] * (n1 // l) and str2 == str2[:l] * (n2 // l):
                    return str1[:l]

if __name__ == '__main__':
    str1 = "ABABABAB"
    str2 = "ABAB"
    sol = Solution()
    print(sol.gcdOfStrings(str1, str2))