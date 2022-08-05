from typing import Counter

class Solution2:
      def getHint(self, secret: str, guess: str) -> str:
		# The main idea is to understand that cow cases contain the bull cases
		# This loop will take care of "bull" cases
        bull=0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])
        
		# This loop will take care of "cow" cases
        cows=0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        return str(bull) + "A" + str(cows-bull) + "B"

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A_count, B_count = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A_count += 1
                guess = guess.replace(secret[i],"$", 1)
                secret = secret.replace(secret[i], "#", 1)
        # print(secret,guess)    
        for j in range(len(secret)):
            if secret[j] in guess:
                B_count += 1
                guess = guess.replace(secret[j],"", 1)
                secret = secret.replace(secret[j], "#", 1)
        # return "%dA%dB" % (A_count, B_count)
        return str(A_count) + "A" + str(B_count) + "B"
        
        
if __name__ == '__main__':
    sol = Solution2()
    secret = "11"
    guess = "10"
    print(sol.getHint(secret, guess))