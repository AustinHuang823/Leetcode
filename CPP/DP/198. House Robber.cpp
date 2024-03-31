class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        else if (nums.size() == 2) return max(nums[0], nums[1]);
        else if (nums.size() == 3) return max(nums[0]+nums[2], nums[1]);
        vector<int> dp = {nums[0], nums[1], nums[0] + nums[2]};
        for (int i = 3; i < nums.size(); i++){
            int prev = dp[1];
            dp[1] = max(dp[0], dp[2]);
            dp[2] = max(prev + nums[i], dp[0] + nums[i]);
            dp[0] = max(dp[0], prev);
        }
        return *max_element(dp.begin(), dp.end());
    }
};