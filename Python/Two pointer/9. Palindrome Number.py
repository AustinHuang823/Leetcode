
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l, r = 0, len(x)-1
        while l < r:
            if x[l] != x[r]:
                break
            else:
                l += 1
                r -= 1
        
        return l >= r



if __name__ == "__main__":
    x = 121
    sol = Solution()
    print(sol.isPalindrome(x))