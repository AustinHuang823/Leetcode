from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        TempArr = []
        for i in range(k+1):
            print(i)
            TempArr.append(sum(cardPoints)-sum(cardPoints[i:len(cardPoints)+i-k]))
            print(TempArr)
        return max(TempArr)
    
class Solution2:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        DI = sum(cardPoints[len(cardPoints)-k:len(cardPoints)]) #Dynamic Index
        Res = DI
        for i in range(k):
            DI = DI + cardPoints[i] - cardPoints[len(cardPoints)-k+i] #update Dynamic Index
            Res = max(Res,DI)
        return Res
        
        
if __name__ == '__main__':
    cardPoints = [1,2,3,4,5,6,1]#[100,40,17,9,73,75]#[96,90,41,82,39,74,64,50,30]#[9,7,7,9,7,7,9]#
    k = 3#3#8#7#
    sol = Solution2()
    print(sol.maxScore(cardPoints,k))
