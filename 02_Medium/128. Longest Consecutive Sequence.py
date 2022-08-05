from typing import List

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        #must be O(n)
        #move nums to a new consecutive array
        #count len and empty it 
        #loop, find max len
        
        max_length =0
        Rearray = []
        while len(nums)> 0:
            min_N = min(nums)
            
            while len(nums)>0:
                Rearray.append(min_N)
                nums.remove(min_N)
                if min_N + 1 in nums: #########O(n^2)
                    min_N = min_N + 1
                else:
                    max_length = max(max_length, len(Rearray))
                    Rearray = []
                    break
            
        return max_length
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #must be O(n)
        #move nums to a new consecutive array
        #count len and empty it 
        #loop, find max len
        h = set()
        for n in nums:
            h.add(n)
        ans = 0
        while h:
            x = h.pop()
            count = 1
            a, b = x-1, x+1
            while a in h:
                count += 1
                h.remove(a)
                a -= 1
            while b in h:
                count += 1
                h.remove(b)
                b += 1
            ans = max(ans, count)
        return ans
        
if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    sol = Solution()
    print(sol.longestConsecutive(nums))