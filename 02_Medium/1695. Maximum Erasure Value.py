from typing import List

class Solution:
    #def maximumUniqueSubarray(self, nums: List[int]) -> int:
    #    TempArray = []
    #    
    #    for r in range(len(nums)):
    #        if nums[r] not in TempArray:
    #            TempArray.append(nums[r])
    #    return sum(TempArray)
    
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        NewArray = set()
        l = 0
        res = 0
        CurSum = 0
        
        for r in range(len(nums)):
            while nums[r] in NewArray and l < r: #meaning it's a duplicate
                NewArray.remove(nums[l])
                CurSum -= nums[l]
                l += 1
            NewArray.add(nums[r])
            CurSum += nums[r]
            res = max(res, CurSum)
            
        return res

if __name__ == "__main__":
    sol = Solution()
    test_1 = ([4,2,1,2,6], 9) #(input, expected result)
    test_2 = ([5,2,1,2,5,2,1,2,5], 8)
    tests = (test_1, test_2)
    for idx, (test_case, expected_result) in enumerate(tests):
        result = sol.maximumUniqueSubarray(test_case)
        print(result)
        if result == expected_result:
            print(f"test {idx + 1} passed")
        else:
            print(f"test {idx + 1} failed")
