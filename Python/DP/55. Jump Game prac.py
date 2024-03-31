
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        if nums_len == 1: return True
        MaxReach = 0
        for i in range(nums_len):
            CanReach = i + nums[i]
            if CanReach > MaxReach:
                MaxReach = CanReach
                if MaxReach >= nums_len - 1:
                    return True 
            if CanReach == i and MaxReach <= i:
                return False 

        # return False
