class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        i = 0
        if word[i].isupper():
            allupper = True
            Firstupper = True
            allnotupper = False
        else:
            allupper = False
            Firstupper = False
            allnotupper = True

        while allupper and i < len(word):
            if not word[i].isupper():
                allupper = False
                break
            i += 1 
        
        i = 1
        while Firstupper and i < len(word):
            if word[i].isupper():
                Firstupper = False
                break
            i += 1 

        i = 1
        while allnotupper and i < len(word):
            if word[i].isupper():
                allnotupper = False
                break
            i += 1 

        return allupper or Firstupper or allnotupper

if __name__ == '__main__':
    word = "FlaG"
    sol = Solution()
    print(sol.detectCapitalUse(word))