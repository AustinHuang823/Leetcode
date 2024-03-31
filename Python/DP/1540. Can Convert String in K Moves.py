class SolutionTLE:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        s, t, visited = list(s),list(t), set()
        
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        dic = {}
        for idx,c in enumerate(alphabets):
            dic[c] = idx

        for c_s, c_t in zip(s,t):
            if c_s != c_t:
                moves = dic[c_t] - dic[c_s]

                if moves < 0:
                    moves += 26
                while moves < k:
                    if moves in visited:
                        moves += 26
                    else:
                        visited.add(moves)
                        break
                if moves > k:
                    return False
            
        return True

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for cs, ct in zip(s, t):
            diff = (ord(ct) - ord(cs)) % 26
            if diff > 0 and cnt[diff] * 26 + diff > k:
                return False
            cnt[diff] += 1
        return True


if __name__ == '__main__':
    s = "aaaaaaa"
    t = "aaaaaaa"
    k = 27
    sol = Solution()
    print(sol.canConvertString(s,t,k))