from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        #create [1,1,1,1,.....,1] because everyone at least need 1 candy
        #check two ways: ratings[i] -> ratings[i+1] & ratings[i+1] -> ratings[i]
        #check if ratings[i] < ratings[i+1], candy_num[i+1] = candy_num[i]+1. do the same thing another way
        n = len(ratings)
        candy_num = [1 for _ in range(n)]
        for i in range(n-1):
            if ratings[i]< ratings[i+1]:
                candy_num[i+1] = candy_num[i] + 1
        print(candy_num)
        for j in reversed(range(n-1)):
            if ratings[j] > ratings[j+1] and candy_num[j] <= candy_num[j+1]: # here we add an additional condition 
                #because candy_num[j] may be already bigger than candy_num[j+1], which will override our previous result
                candy_num[j] = candy_num[j+1] + 1
        print(candy_num)
        return sum(candy_num)
    
        
            


if __name__ == '__main__':
    ratings = [1,3,4,5,2]#[1,2,87,87,87,2,1]#[1,3,2,2,1]#[1,0,2]#[1,2,2]
    sol = Solution()
    print(sol.candy(ratings))