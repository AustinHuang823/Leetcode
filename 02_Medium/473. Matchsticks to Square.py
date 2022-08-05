from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if len(matchsticks) < 4 : return False
        sumn = sum(matchsticks)
        matchsticks.sort(reverse=True)
        if sumn % 4 != 0: return False
        target = [sumn/4] * 4
        
        def dfs(matchsticks, pos, target):
            if pos == len(matchsticks): return True
            
            for i in range(4):
                if target[i] >= matchsticks[pos]:
                    target[i] -= matchsticks[pos]
                    print(target)
                    if dfs(matchsticks, pos+1, target): 
                        return True
                    target[i] += matchsticks[pos]
            return False
        
        return dfs(matchsticks,0, target)

        
if __name__ == '__main__':
    matchsticks1 = [1,1,2,2,2]
    matchsticks2 = [3,3,3,3,4]
    matchsticks3 = [5,5,5,5,4,4,4,4,3,3,3,3]
    sol = Solution()
    # print(sol.makesquare(matchsticks1), sol.makesquare(matchsticks2),sol.makesquare(matchsticks3))
    print(sol.makesquare(matchsticks3))