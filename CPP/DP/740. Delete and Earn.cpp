class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        map<int, int> counter;
        for (int n: nums) counter[n]++; //log(n)
        for (auto& p: counter) counter[p.first] = p.first * p.second;
        int prev = -1;
        vector<int> dp = {0,0,0};
        for (auto& p: counter){
            int curr = p.first;
            if(prev+1 == curr){
                int prevsum = dp[1];
                dp[1] = max(dp[0], dp[2]);
                dp[2] = max(dp[0] + p.second, prevsum + p.second);
                dp[0] = max(dp[0], prevsum);
            }
            else{
                int prevsum = dp[1];
                dp[1] = max(dp[0], dp[2]);
                dp[2] = max({dp[0] + p.second, prevsum + p.second, dp[2] + p.second});
                dp[0] = max(dp[0], prevsum);
            }
            prev = curr;
        }
        return *max_element(dp.begin(), dp.end());
    }
};