class Solution:
    def pivotInteger(self, n: int) -> int:

        # we have two arithmetic sequences
        # sums are for the left and the right ones correspondingly :
        # 0.5 * (1 + n) * n
        # 0.5 * (n + m) * (m - n + 1)

        # so the solution is the following:
        result = ((n ** 2 + n) * 0.5) ** 0.5
        rounded = int(result)

        if rounded == result:
            return rounded

        return -1

if __name__ == '__main__':
    n = 8
    sol = Solution()
    print(sol.pivotInteger(n))