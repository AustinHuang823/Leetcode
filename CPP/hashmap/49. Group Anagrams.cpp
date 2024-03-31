class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dict;
        for (string s: strs){
            string key = s;
            sort(key.begin(), key.end());
            dict[key].push_back(s);
        }
        vector<vector<string>> res;
        for (auto p: dict){
            res.push_back(p.second);
        }
        return res;
    }
};