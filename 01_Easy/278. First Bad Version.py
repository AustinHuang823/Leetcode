# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #we conduct a binary search here
        path = 0
        while n:
            pivot = n//2
            if isBadVersion(path + pivot) == False:
                n -= pivot
                path += pivot
            elif isBadVersion(path + pivot) == True:
                n = pivot
            if pivot == 0: break
                
        return path+1 # path will always convergence at the last False, 
                      #     because we never renew it when isBadVersion() == True, so we return path +1 here
                
            