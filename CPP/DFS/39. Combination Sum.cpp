class Solution {
public:
    vector<vector<int>> ans;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        ans.clear();

        vector<int> temp;

        solve(0, candidates, temp, target);

        return ans;
    }
    void solve(int start, vector<int>& candidates, vector<int>& temp, int target){
        if(target == 0){
            ans.push_back(temp);
            return;
        }

        if(target < 0)
            return;
        
        for(int i=start; i<candidates.size(); i++){
            temp.push_back(candidates[i]);
            solve(i, candidates, temp, target - candidates[i]);
            temp.pop_back();
        }

    }
};