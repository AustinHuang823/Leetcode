
class Solution:
    def shortestWordEditPath(self, source, target, words):
        words = set(words)
        
        q = [(source, 0)]
        visisted = set()
        while q:
            aWord, aStep = q.pop()
            visisted.add(aWord)
            if aWord == target: return aStep
            
            aWordList = list(aWord)
            for i, letter in enumerate(aWordList):
                for sub in "abcdefghijklmnopqrstuvwxyz":
                    if letter == sub: continue
                    temp = aWordList[:] #O(len(temp))
                    temp[i] = sub
                    tempWrd = "".join(temp)
                    if tempWrd in words and tempWrd not in visisted:
                        q.append((tempWrd, aStep + 1))
        
        return -1
        
if __name__ == '__main__':
    source = "bit"
    target = "dog"
    words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
    sol = Solution()
    ans = sol.shortestWordEditPath(source, target, words)
    print(ans)