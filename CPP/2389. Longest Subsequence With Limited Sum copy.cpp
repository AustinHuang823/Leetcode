class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        int n = queries.size();
        sort(nums.begin(),nums.end());
        vector<int> prefix = nums;
        for (int i = 1; i < prefix.size(); i++) prefix[i] = prefix[i]+ prefix[i-1];
        vector<int> res(n);
        for (int i = 0; i < n; i++){
            int& k = queries[i];
            for (int end = prefix.size()-1; end >= 0; end--){
                if (prefix[end] <= k) {
                    res[i] = end+1;
                    break;
                }
            }
        }
        return res;
    }
};