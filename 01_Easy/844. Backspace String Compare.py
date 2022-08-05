class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
       
        record_s, record_t = [], []
        for i in range(len(s)):
            if s[i] == "#":
                record_s.append(i)
        
        cc = 0
        for j in range(len(record_s)):
            record_s[j] -= cc
            if record_s[j] == 0: 
                s = s[1:]
                cc += 1
            elif j < len(record_s):
                s = s[:record_s[j]-1] + s[record_s[j]+1:] 
                cc += 2
            
            
            
        for i in range(len(t)):
            if t[i] == "#":
                record_t.append(i)
                
        tc = 0
        for j in range(len(record_t)):
            record_t[j] -= tc
            if record_t[j] == 0: 
                t = t[1:]
                tc += 1 
            elif j < len(record_t): 
                t = t[:record_t[j]-1] + t[record_t[j]+1:]  
                tc += 2

            
        return (s == t)
        
        
if __name__ == '__main__':
    sol = Solution()
    s = "a##c"
    t = "#a#c"
    print(sol.backspaceCompare(s,t))