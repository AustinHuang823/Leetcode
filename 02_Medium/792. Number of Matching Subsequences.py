from typing import List
import collections

class Solution2:
    def numMatchingSubseq(self, S, words):
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        originS = s
        for i in range(len(words)):
            s = originS
            for j in range(len(words[i])+1):
                if j == len(words[i]): 
                    count += 1
                    break
                if words[i][j] in s:
                    s = s[s.index(words[i][j])+1:]
                else: break
                
        return count

if __name__ == '__main__':
    sol = Solution2()
    s = "abcde"
    words = ["a","bb","acd","ace"]
    print(sol.numMatchingSubseq(s, words))