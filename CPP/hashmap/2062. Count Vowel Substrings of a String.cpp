class Solution {
public:
    int countVowelSubstrings(string word) {
        int res = 0;
        for (int i = 0; i < (word.size()-4); i++){
            for (int j = (i+4); j <= word.size(); j++){
                // string s = word.substr(i, j);
                // cout << i << j << endl;
                string s(word.begin()+i, word.begin()+j);
                if (ifvalid(s)) {
                    cout << s << endl;
                    res++;
                }
            }
        }
        return res;
    }

    bool ifvalid(string& s){
        unordered_map<char, int> vow_count;
        for (char c: s){
            vow_count[c]++;
        }
        if (vow_count['a'] < 1 || vow_count['e'] < 1 || vow_count['i'] < 1 || vow_count['o'] < 1 || vow_count['u'] < 1) return false;
        for (pair<char, int> p: vow_count){
            if (p.first != 'a' && p.first != 'e' && p.first != 'i' && p.first != 'o' && p.first != 'u') return false;
        }
        return true;
    }
};