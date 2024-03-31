class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0, curEnd = 0, curReach = 0, goal = nums.size()-1;
        for (int i = 0; i <= goal; i++){
            curReach = max(curReach, i + nums[i]);
            if (curEnd == goal) return jumps;
            if (i == curEnd) {
                jumps++;
                curEnd = curReach;
            }
        }
        return jumps;
    }
};