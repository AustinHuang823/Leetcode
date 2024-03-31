class Solution {
public:
    vector<string> letterCombinations(string digits) {
        unordered_map<char, vector<string>> map;
        map['2'] = {"a","b","c"};
        map['3'] = {"d","e","f"};
        map['4'] = {"g","h","i"};
        map['5'] = {"j","k","l"};
        map['6'] = {"m","n","o"};
        map['7'] = {"p","q","r","s"};
        map['8'] = {"t","u","v"};
        map['9'] = {"w","x","y","z"};

        vector<string> temp;
        vector<string> temp_res;
        vector<string> res;
        for (int i = 0; i < digits.size(); i++){
            for (string c: map[digits[i]]){
                temp.push_back(c);
            }
            if (res.size() == 0) res = temp;
            else {
                for (string sr: res){
                    for (string st: temp) {
                        temp_res.push_back(sr + st);
                    }                    
                }
                res = temp_res;
                temp_res.clear();
            }
            temp.clear();
        }
        return res;
    }
};