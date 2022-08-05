from typing import List #vscode line
class Solution:
    def fib(self, n: int) -> int:
        #in fib array, we need to give F(0) and F(1) definition because F(n) always comes with F(n-2) and F(n-1),
        #that means at F(0) and F(1), if we use the function, we'd reach F(-2) and F(-1), which are not in the case.
        
        fib_array = [0,1] #giving definition of F(0) and F(1)
        if n ==0: return 0
        elif n == 1: return 1 #2 cases that we don't want to use our fib function
        
        else:
            for i in range(2,n+1): #use n+1 for right edge because the code only run to (n+1)-1 here
                fib_array.append(fib_array[i-2] + fib_array[i-1]) # F(i) = F(i-1) + F(i-2)
        
        return fib_array[-1] #Return the last number of fib_array
                    
                

if __name__ == '__main__': #vscode main line
    sol = Solution()
    n = 20
    print(sol.fib(n))