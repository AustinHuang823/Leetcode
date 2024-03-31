from typing import List
import collections
class SolutionTLE:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums[:k])
        CurSum = sum(nums[:k])
        res = 0
        
        for n in counter.values():
            if n >= 2:
                break
        else:
            res = CurSum
        
        for i in range(len(nums)-k):
            if nums[i] == nums[i+k]:
                continue
            CurSum = CurSum - nums[i] + nums[i+k]
            counter[nums[i]] -= 1
            if nums[i+k] in counter:
                counter[nums[i+k]] += 1
            else:
                counter[nums[i+k]] = 1
            
            if counter[nums[i]] == 0:
                counter.pop(nums[i])
            
            for n in counter.values():
                if n >= 2:
                    break
            else:
                res = max(res, CurSum)
        
        return res

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res, cur, pos, dup = 0, 0, [-1] * 10, -1
        for i in range(0,len(nums)):
            cur += nums[i]                      # compute running sum for
            if i >= k: cur -= nums[i-k]         # the window of length k
            
            dup = max(dup, pos[nums[i]])        # update LAST seen duplicate
            
            if i - dup >= k:                    # if no duplicates were found
                res = max(res, cur)             # update max window sum

            pos[nums[i]] = i

        return res

    
if __name__ == '__main__':
    nums = [1,5,4,2,9,9,9]
    k = 3
    sol = Solution()
    print(sol.maximumSubarraySum(nums, k))