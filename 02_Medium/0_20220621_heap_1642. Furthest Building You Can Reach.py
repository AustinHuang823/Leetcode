from typing import List
######Should check for heap solution after taking the course#####
class Solution: ##time exceeds limit
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        CH = [] #Climbed Height [8, 5, 15, 2, 16]  // 5 3 5
        for i in range(len(heights)-1):
            if heights[i+1] - heights[i] > 0:
                CH.append(heights[i+1] - heights[i])
        HD = [] #[-2, 5, -1, 3, 5, -2]
        for i in range(len(heights)-1):
            HD.append(heights[i+1] - heights[i])
        
        CHs = sorted(CH)    #sort CH to find biggest CH
        if ladders == 0:     #CHs considering Ladder
            CHsL = CHs
        else:
            CHsL = CHs[:-ladders] 
              
        if sum(CHsL) <= bricks:     #cases make to the end
            return len(heights) - 1

        elif bricks == 0 and ladders == 0: #in cases that we don't have any b and l
            count2 = 0
            for l, r in enumerate(HD):
                if r < 0:
                    count2 += 1
            return count2


        else:                       #cases that can't make to the end
            for j in range(len(CH)):
                stCH = sorted(CH[0:j+1])
                laddercost = sum(stCH)-sum(stCH[:-ladders])
                if sum(CH[0:j+1]) - laddercost > bricks:
                    count = 0
                    for n, m in enumerate(HD):  #0 -2, 1 5, 2 -1, 3 3, 4 5, 5 -2 
                        if m > 0:
                            count += 1
                            if count - 1 == j and m == CH[j]:
                                return n

class Solution2: #Binary Search
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # return max if we have enough ladders
        length = len(heights)
        if ladders == length: return length-1
        
        #
        # def helper function canIReach(List, l, b): return true if I can, return false if I can not
        #
        def canIReach(mylist, l, b):
            if mylist == None:
                mylist = hdef
            mylist.sort()
            if l==0:
                test = mylist
            else:
                test = mylist[:-l]
            
            if b >= sum(test):
                return True
            else:
                return False

        # hdef this is the list of [#bricks needed to get to next building]
        # bum is the list of [building # that need either bricks or ladders]
        hdef= []
        bnum=[]
        for i in range(length-1):
            dif = heights[i]-heights[i+1]
            if dif < 0:
                hdef.append(-dif)
                bnum.append(i)
                
        # if we have more ladders, return max
        if len(hdef) <= ladders: return length-1
        # Otherwise, we compare from hdef[ladders:] do a binary search:
        
        left = ladders
        right = len(hdef)
        
        while (left< right):
            mid = left + (right-left)//2
            
            if (canIReach(hdef[:mid+1],ladders,bricks)):
                left = mid+1
            else:
                right = mid
        
        # now left is last building that we can reach with a tool
        if left >= len(hdef): return length-1
        return bnum[left]



        

        #find climb height in list "heights"


if __name__ == '__main__':
    heights = [4,2,7,6,9,14,12]
    bricks = 5
    ladders = 1
    sol = Solution2()
    print(sol.furthestBuilding(heights, bricks, ladders))
