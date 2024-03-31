class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int curSum = 0, maxSub = INT_MIN;
        for (int i = 0; i < n; i++){
            curSum += nums[i];
            maxSub = max(curSum, maxSub);
            curSum = max(curSum, 0);
        }
        return maxSub;
    }
};