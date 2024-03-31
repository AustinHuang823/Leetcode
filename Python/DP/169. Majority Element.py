from typing import List

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter[n] += 1

        max_count, major_ele = float('-inf'), None
        for n, count in zip(counter.keys(), counter.values()):
            if count > max_count:
                max_count = count
                major_ele = n
        
        return major_ele
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj_ele = None

        for n in nums:
            if count == 0:
                maj_ele = n
                count += 1
            elif maj_ele == n:
                count += 1
            else:
                count -= 1
        return maj_ele

if __name__ == '__main__':
    nums = [2,2,1,1,1,2,2]
    sol = Solution()
    print(sol.majorityElement(nums))