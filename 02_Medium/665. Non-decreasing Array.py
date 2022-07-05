from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dc = 0 #decrease count
        # 2cases, len(nums) <=2 >2
        if len(nums) <= 2:
            return True


        if len(nums) > 2:
            # for idx,ele in enumerate(nums):
            #     # print(i)
            #     if idx < len(nums)-1:
            #         if nums[idx] > nums[idx+1]:
            #             for j in range(len(nums)):
            #                 if nums[idx]<nums[j]:
            #                     nums.insert(j, nums[idx])
            #                     nums.remove(nums[idx])
            #                     dc += 1 
            #                     print(nums)
            #                 elif nums[idx] == max(nums):
            #                     nums.append(nums[idx])
            #                     nums.remove(nums[idx])
            #                     dc += 1
            #                     print(nums)
            #                 break                 this method would have issue when [4,3,2], which doesn't modify the 0 ele
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    dc += 1
                    if i==0 or nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i+1]#modify nums[i]
                    else:
                        nums[i+1] = nums[i]#modify nums[i+1]
                    # print(nums)

                    
        return dc <= 1

            

if __name__ == '__main__':
    nums =  [3,4,3]
    sol = Solution()
    print(sol.checkPossibility(nums))