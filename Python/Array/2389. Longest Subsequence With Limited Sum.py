from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        increase_nums = sorted(nums)
        res = []
        for max in queries:
            temp_sum = 0
            for i in range(len(increase_nums)):
                temp_sum += increase_nums[i]
                if temp_sum > max:
                    res.append(i)
                    break
                if i+1 == len(increase_nums):
                    res.append(i+1)
        return res

if __name__ == '__main__':
    nums = [4,5,2,1]
    queries = [3,10,21]
    sol = Solution()
    print(sol.answerQueries(nums, queries))