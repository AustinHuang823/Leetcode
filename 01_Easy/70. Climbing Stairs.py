class Solution2: # time limit exceeded
    def climbStairs(self, n: int) -> int:
        def dfs(pos):
            if pos < n:
                return dfs(pos+1) + dfs(pos+2)
            if pos == n:
                return 1
            return 0
        
        if n > 0:
            return dfs(0)
        
        
class Solution:
    """The problem seems to be a dynamic programming one. Hint: the tag also suggests that!
        Here are the steps to get the solution incrementally.

        Base cases:
        if n <= 0, then the number of ways should be zero.
        if n == 1, then there is only way to climb the stair.
        if n == 2, then there are two ways to climb the stairs. One solution is one step by another; the other one is two steps at one time.

        The key intuition to solve the problem is that given a number of stairs n, if we know the number ways to get to the points [n-1] and [n-2] respectively, denoted as n1 and n2 , then the total ways to get to the point [n] is n1 + n2. Because from the [n-1] point, we can take one single step to reach [n]. And from the [n-2] point, we could take two steps to get there.

        The solutions calculated by the above approach are complete and non-redundant. The two solution sets (n1 and n2) cover all the possible cases on how the final step is taken. And there would be NO overlapping among the final solutions constructed from these two solution sets, because they differ in the final step.

        Now given the above intuition, one can construct an array where each node stores the solution for each number n. Or if we look at it closer, it is clear that this is basically a fibonacci number, with the starting numbers as 1 and 2, instead of 1 and 1.
    """
    def climbStairs(self, n: int) -> int:
        
        fib_array = [0,1] #giving definition of F(0) and F(1)
        if n ==0: return 0
        elif n == 1: return 1 #2 cases that we don't want to use our fib function
        
        else:
            for i in range(2,n+2): #use n+1 for right edge because the code only run to (n+1)-1 here
                fib_array.append(fib_array[i-2] + fib_array[i-1]) # F(i) = F(i-1) + F(i-2)
        
        return fib_array[-1] #Return the last number of fib_array
        
if __name__ == '__main__':
    sol = Solution()
    n = 15
    print(sol.climbStairs(n))