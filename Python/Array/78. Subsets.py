from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def dfs(nums, path, ret):
            ret.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]], ret)

        dfs(nums, [], ret)
        return ret


if __name__ == '__main__':
    nums = [1,2,3]
    sol = Solution()
    print(sol.subsets(nums))