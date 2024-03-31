class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size(), maxlen = INT_MIN, start = 0, zeroCounter = 0;
        for (int end = 0; end < n; end++){
            if (nums[end] == 0) zeroCounter++;

            while (zeroCounter > k){
                if (nums[start++] == 0) zeroCounter--;
            }
            maxlen = max(maxlen, end-start+1);
        }
        return maxlen;
    }
};