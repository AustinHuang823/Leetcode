from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the people from tall to short
        # insert from tall to short (insert at index = p[1])
        people.sort(key=lambda p: (-p[0],p[1]))
        res = []
        # print(people)
        for p in people:
            res.insert(p[1],p)
        return res
        
if __name__ == '__main__':
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    sol = Solution()
    print(sol.reconstructQueue(people))