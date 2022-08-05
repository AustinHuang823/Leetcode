from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        arr = [i for i in range(len(s)+1)]
        ans = []
        for j in range(len(s)):
            if s[j] == "D":
                ans.append(arr[-1])
                arr.remove(arr[-1])
            if s[j] == "I":
                ans.append(arr[0])
                arr.remove(arr[0])
        ans.append(arr[0])
        return ans



if __name__ == '__main__':
    sol = Solution()
    s = "IDID"
    print(sol.diStringMatch(s))