class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = nums.size()-1;
        for (int i = nums.size() - 2; i >= 0; i--){
            if (i + nums[i] >= goal) goal = i;
        }
        return goal == 0;
    }
};

class Solution2 {
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