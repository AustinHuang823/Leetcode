from typing import List
import collections
import heapq

class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # table = {}
        # for word in words:
        #     if word in table:
        #         table[word] += 1
        #     else:
        #         table[word] = 1
        table = collections.Counter(words)
        # set up a max heap
        heap = []
        heapq.heapify(heap)
        for key in table:
            heapq.heappush(heap, (-table[key], key))
        # pop top k
        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped)
            
        # sort res alphabetically
        res.sort()
        newres = []
        for word in res:
            newres.append(word[1])
        return newres
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        # print(count)
        y = sorted(count.items(), key=lambda x:(-x[1],x[0]))
        # print(y)
        
        return [i[0] for i in y][:k]
        
if __name__ == '__main__':
    words = ["aaa","aa","a"]
    k = 1
    sol = Solution2()
    print(sol.topKFrequent(words,k))