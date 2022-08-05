from typing import List
import collections
class Solution2:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        target = {}
        for targetWord in words2:
            toAdd = {}
            for letter in targetWord:
                if letter not in toAdd:
                    toAdd[letter] = 1
                else:
                    toAdd[letter] += 1
            
            for letter, occur in toAdd.items():
                if letter in target:
                    target[letter] = max(occur, target[letter])
                else:
                    target[letter] = occur
        ret = []
        for a in words1:
            toInclude = True
            for key in target:
                if a.count(key) < target[key]:
                    toInclude = False
                    break
            if toInclude:
                ret.append(a)
        return ret



class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        temp_str = ""
        for w in words2:
            temp_str = temp_str + w
        check = collections.Counter(temp_str)
        res = []
        for word in words1:
            Toinclude = True
            for key in check:
                if word.count(key) < check[key]:
                    Toinclude = False
                    break
            if Toinclude:
                res.append(word)
        return res
            




if __name__ == '__main__':
    sol = Solution2()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo","eo"]
    print(sol.wordSubsets(words1, words2))