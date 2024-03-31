import collections
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        right = collections.deque(s)
        left = []
        res = 0
        while right:
            this = right.popleft()
            if this == '(':
                left.append(this)
            elif this == ')':
                if not left:
                    res += 1
                else:
                    left = left[1:]
        return res + len(left)

if __name__ == '__main__':
    s = "()))(("
    sol = Solution()
    print(sol.minAddToMakeValid(s))