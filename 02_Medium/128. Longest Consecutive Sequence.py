from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #must be O(n)
        #move nums to a new consecutive array
        #count len and empty it 
        #loop, find max len
        
        max_length =0
        Rearray = []
        while len(nums)> 0:
            min_N = min(nums) #O(n)
            
            while len(nums)>0:
                Rearray.append(min_N)
                nums.remove(min_N)
                if min_N + 1 in nums: #O(n)
                    min_N = min_N + 1
                else:
                    max_length = max(max_length, len(Rearray))
                    Rearray = []
                    break
            
        return max_length
        
if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    sol = Solution()
    print(sol.longestConsecutive(nums))
