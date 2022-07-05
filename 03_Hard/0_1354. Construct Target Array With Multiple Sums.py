from typing import List
import heapq
##check heap solution

class Solution:

    def isPossible(self, target: List[int]) -> bool:
        def get_max(target):
            maximum = 0
            for ele in target:
                if ele > maximum:
                    maximum = ele
            return maximum
        
        def recurse(target):
            sumt = sum(target)
            if sumt == len(target):
                return True
            else:
                maximum = get_max(target)
                pivot = sumt - maximum
                if pivot == 0:   # can't reduce further
                    return False
                for idx, ele in enumerate(target):
                    if ele > pivot:
                        target[idx] = ele - pivot
                        # print(target)
                        return recurse(target)
                return False
        return recurse(target)

class Solution2:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-a for a in target]
        heapq.heapify(target)
        while True:
            a = -heapq.heappop(target)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(target, -a)




if __name__ == '__main__':
    sol = Solution2()
    target = [1,1000000000] #p5[2,3][1,2]
    print(sol.isPossible(target))