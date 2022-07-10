
from multiprocessing.sharedctypes import Value
from typing import List

class Solution_Brute:
    def maxProfit(self, prices: List[int]) -> int:

        maxvalue = float('-inf')
        for i in range(len(prices)-1):      #O(n)
            maxNum = max(prices[i+1:])      #O(n) 
            #combining with the for loop & min() in the previous 2 line. Time complexity here is O(n^2)
            maxvalue = max(maxNum - prices[i], maxvalue)#O(2)
        
        if maxvalue < 0:
            return 0
        return maxvalue #O(1)
        ### THe Time complesxity here is O(n^2)

    
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            money, Value = float('inf'), 0
            for p in prices:    #O(n)
                if p < money:   #O(1)
                    money = p                 
                if p - money > Value : 
                    Value = p - money   #O(1)
            return Value    #O(1)
            ###The Time complexity here is O(n)

        
if __name__ == '__main__': 
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))