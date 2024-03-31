from typing import List
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """ 
        i, j = 0, 0
        
        output = []
        
        while j < len(chars):
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            
            output.append(chars[i])
            if i+1 != j:
                for c in str(j-i):
                    output.append(c)
                
            i = j
            
        chars[:] = output
        return len(output)
                


if __name__ == "__main__":
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    sol = Solution()
    print(sol.compress(chars))