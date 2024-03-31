class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int L = nums.size();

        k = k % L;
        reverse(nums.begin(), nums.end());

        for (int i = 0; i < k/2; i++){
            int temp = nums[i];
            nums[i] = nums[k-i-1];
            nums[k-i-1] = temp;
        }

        for (int i = 0; i < (L-k)/2; i++){
            int temp = nums[k+i];
            nums[k+i] = nums[L-i-1];
            nums[L-i-1] = temp;
        }
    }
};