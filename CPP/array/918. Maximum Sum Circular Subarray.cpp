class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n = nums.size();
        int maxCur = 0, maxSub = INT_MIN;
        int minCur = 0, minSub = INT_MAX;
        int total = 0;
        for (int i = 0; i < n; i++){
            maxCur += nums[i];
            maxSub = max(maxSub, maxCur);
            maxCur = max(maxCur, 0);

            minCur += nums[i];
            minSub = min(minSub, minCur);
            minCur = min(minCur, 0);

            total += nums[i];
        }
        return maxSub > 0 ? max(maxSub, total - minSub): maxSub;
    }
};