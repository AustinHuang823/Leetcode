class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l < r){
            // cout << (l+r)/2 << endl;
            int mid = (l+r)/2;
            if (nums[mid] < target){
                l = (l+r)/2 + 1;
            }
            else if (nums[mid] >= target){
                r = (l+r)/2;
            }
        }
        return nums[l]==target ? l: -1;
        // return l;
    }
};