class Solution {
public:
    bool canJump(vector<int>& nums) {
        int curEnd = 0, curReach = 0, goal = nums.size()-1;
        for (int i = 0; i <= goal; i++){
            curReach = max(curReach, i + nums[i]);
            if (curReach >= goal) return true;
            if (curReach == i && nums[i] == 0) return false;
        }
        return true;
    }
};