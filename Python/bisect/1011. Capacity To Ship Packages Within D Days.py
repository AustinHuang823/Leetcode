from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need_days, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need_days += 1
                    cur = 0
                cur += w
            if need_days > days: left = mid + 1
            else: right = mid
        return int(left)


if __name__ == '__main__':
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    sol = Solution()
    print(sol.shipWithinDays(weights, days))