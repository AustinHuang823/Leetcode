from typing import List
import collections

class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        cnt= collections.Counter(nums)
        counts = []
        for i in range(len(nums)):
            if nums[i] in cnt:
                cnt[nums[i]] -= 1
                count = 0
                for n in cnt:
                    if n < nums[i]:
                        count += cnt[n]
                counts.append(count)
                
        return counts
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        cnt= collections.Counter(nums)
        counts = []
        y = sorted(cnt.items(), key=lambda x:(-x[0]))

        for i in range(len(nums)):
            if nums[i] in cnt:
                cnt[nums[i]] -= 1
               
                # I think below is the line need to fix
                counts.append(sum([j[1] for j in y]))
                print("here for nums[i] ==",nums[i],",I want to sum y[1] right to y[0] ==", nums[i],"in", y)
                
        return counts
        
if __name__ == '__main__':
    nums = [5,2,6,1]
    sol = Solution()
    print("ans ==", sol.countSmaller(nums),"which is wrong, for this specific case, ans should be [2,1,1,0]")