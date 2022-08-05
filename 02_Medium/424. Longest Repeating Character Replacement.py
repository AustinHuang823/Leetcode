import collections
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Max_length the longest subsequence without repeating chars and k changes
        # Max_count is the high count chars in the answer subsequence
        max_length = max_count = 0
        # Count keeps track of the chars in the we are looking at subsequence
        count = defaultdict(int)
        
        for i in range(len(s)):
            # Add char to the count dict
            count[s[i]] += 1
            # key idea(2): Find the new max_count. This is much like Kadane's
            # Where we only consider if the new length exceedes the max_length overall
            max_count = max(max_count, count[s[i]])
            
            # Key idea (1): the answer is always max_count + k.
            if max_length < k + max_count:
                max_length += 1
            else:
                # key idea(3) This removes the char at the start of the subsequence s[i-max_length]
                # This serves as "correction" for the subsequence problem
                count[s[i-max_length]] -= 1
        return max_length
    

class Solution2: # time limit exceeded DFS
    def characterReplacement(self, s: str, k: int) -> int:
        return self.dfs(0, len(s), k, {}, s)
        
    def dfs(self, l, r, k, dp, s):
        if len(set(s[l:r])) <= k+1: 
            tempcounter = []
            s_temp = s[l:r]
            s_set = set(s_temp)
            for c in s_set:
                tempcounter.append(s_temp.count(c))
            if sum(tempcounter) - max(tempcounter) <= k:
                return r - l
        if (l,r) in dp: return dp[(l,r)]
        if l >= r : return 0
        dp[(l,r)] = max(self.dfs(l+1, r, k, dp, s), self.dfs(l, r-1, k, dp, s))
        return dp[(l,r)]
        
if __name__ == '__main__':
    sol = Solution()
    s = "BAAAABCDE"
    k = 2
    print(sol.characterReplacement(s,k))