class Solution {
public:
    string greatestLetter(string s) {
        string res = "";
        vector<int> upp(26), low(26);
        for (char c: s){
            if (c-'A' >= 0 && c-'A' <= 25) upp[c-'A']++;
            else low[c-'a']++;
        }

        for (int i = 25; i >= 0; i--){
            if (upp[i] && low[i]) {
                res += 'A'+i;
                return res;
            }
        }
        return "";
    }
};