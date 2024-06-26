class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman_int_map {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };

        int res = 0;
        for (int i = 0; i < s.size(); i++){
            if (roman_int_map[s[i]] < roman_int_map[s[i+1]]){
                res += roman_int_map[s[i+1]] - roman_int_map[s[i]];
                i++;
            }
            else {
                res += roman_int_map[s[i]];
            }
        }
        return res;
    }
};