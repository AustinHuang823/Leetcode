from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        LoseCount = {}
        for match in matches:
            if match[0] not in LoseCount:
                LoseCount[match[0]] = 0
            if match[1] not in LoseCount:
                LoseCount[match[1]] = 1
            else:
                LoseCount[match[1]] += 1

        res = [[],[]]
        for player in LoseCount:
            if LoseCount[player] == 0:
                res[0].append(player)
            elif LoseCount[player] == 1:
                res[1].append(player)
        res[0] = sorted(res[0])
        res[1] = sorted(res[1])
        return res


if __name__ == "__main__":
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    sol = Solution()
    print(sol.findWinners(matches))