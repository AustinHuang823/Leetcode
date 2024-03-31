class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cur_reach = 0
        next_max_reach = 0
        jumps = 0

        for i in range(n):
            if i > cur_reach:
                jumps += 1
                cur_reach = next_max_reach
            next_max_reach = max(i + nums[i], next_max_reach)
        
        return jumps