from typing import List

class Solution2: #doesn't fit certain specific case
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) == len(t) == 1:
            return True
        
        s_count, t_count = 1, 1
        for i in range(1,len(s)+1):
            if i == len(s):
                return True
            
            if s[i] == s[i-1]:
                s_count += 1
            elif s[i] != s[i-1]:
                s_count = 1
            
            if t[i] == t[i-1]:
                t_count += 1
            elif t[i] != t[i-1]:
                t_count = 1
                
            if s_count != t_count:
                return False
        

class Solution: 
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_CArray, t_CArray = [], [] # establish 2 list here to store repeated characters
        for i in range(len(s)+1): 
            if i == len(s):
                return True
            # here we use a little trick here: once i reach length of string, means that the entire string of s & t have pass our test
            # also the constraint says that len(s) == len(t), so we set the right edge at len(s)+1, which only runs to len(s)
 
            if s[i] not in s_CArray:
                s_CArray.append(s[i])
            # checking if the character isn't in our Array, add it at the end

            if t[i] not in t_CArray:
                t_CArray.append(t[i])
            
            if s_CArray.index(s[i]) != t_CArray.index(t[i]):
                return False
            # here's our test method. Once the element structure of string is different, the position of the element in our storing array would be different
            # if you try to check the length here, that wouldn't work. try testcase: s = "abcda", t = "abcdb" . You'll find that although the length of s_CArray == t_CArray, the structures are different, which we should return a False here.
        




if __name__ == '__main__': #vscode main line
    sol = Solution()
    s = "abcda"
    t = "abcdb"
    print(sol.isIsomorphic(s,t))