from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                N = w[i:]
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)
        



if __name__ == '__main__':
    words = ["time", "me", "bell"]
    sol = Solution()
    print(sol.minimumLengthEncoding(words))