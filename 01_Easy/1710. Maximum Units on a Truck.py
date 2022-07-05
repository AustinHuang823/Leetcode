from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (-x[1])) #Sort reversly so we can always start with biggest numberOfUnitsPerBox with the smallest i in boxTypes
        boxCount = 0 #our total occupied box
        Res = 0 #our answer
        for i in range(len(boxTypes)):  # for loop to fill up the truck with boxes
            if boxCount < truckSize:
                boxCount += boxTypes[i][0]
                Res += boxTypes[i][0]*boxTypes[i][1]
            if boxCount > truckSize: break
            
        if boxCount < truckSize: #for the cases that we can put all the box in the truck
            return Res
        else:
            Res -= (boxCount - truckSize) * boxTypes[i][1] #for the cases that we overfill the truck
        return Res



if __name__ == '__main__':
    sol = Solution()
    boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]#[[5,10],[2,5],[4,7],[3,9]]#[[1,3],[2,2],[3,1]]
    truckSize = 35#10#4
    print(sol.maximumUnits(boxTypes,truckSize))