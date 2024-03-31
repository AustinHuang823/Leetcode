class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        all_c = "abcdefghijklmnopqrstuvwxyz"
        dic = {}
        for c in all_c:
            dic[c] = 0
        for c1 in s1:
            dic[c1] += 1

        for c_int in s2[:len(s1)]:
            dic[c_int] -= 1
        if self.detectnot0(dic.values()):
            return True

        for i in range(len(s1), len(s2)):
            dic[s2[i-len(s1)]] += 1
            dic[s2[i]] -= 1
            if self.detectnot0(dic.values()):
                return True
                
        return False
    
    def detectnot0(self, val_list):
        for n in val_list:
            if n != 0: return False
        return True



if __name__ == '__main__':
    s1 = "a"
    s2 = "ab"
    sol = Solution()
    print(sol.checkInclusion(s1,s2))