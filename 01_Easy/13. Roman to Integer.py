class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_dict = {"I":1, "V": 5,"X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        Roman2_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        ans = 0
        for key in Roman2_dict:
            if key in s:
                ans += Roman2_dict[key]
                s = s.replace(key, "", 1)
        
        for c in s:
            ans += Roman_dict[c]
        
        return ans
        
if __name__ == '__main__':
    s = "MCMXCIV"
    sol = Solution()
    print(sol.romanToInt(s))