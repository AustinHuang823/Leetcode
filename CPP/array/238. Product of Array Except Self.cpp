class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product_from_left = 1, product_from_right = 1;
        int len_nums = nums.size();
        vector<int> res(len_nums, 1);
        for (int i = 0; i < len_nums - 1; i++){
            product_from_left *= nums[i];
            res[i+1] *= product_from_left;
        }
        for (int i = len_nums - 1; i > 0; i--){
            product_from_right *= nums[i];
            res[i-1] *= product_from_right;
        }

        return res;
    }
};