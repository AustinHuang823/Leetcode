from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for idx, c in enumerate(order):
            order_map[c] = idx

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False

        return True
if __name__ == '__main__':
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    sol = Solution()
    print(sol.isAlienSorted(words, order))