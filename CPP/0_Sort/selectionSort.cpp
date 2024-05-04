#include <vector>
using namespace std;

/*
Time: nlogn
Space: n
*/

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            int minIdx = i;
            for (int j = i+1; j < nums.size(); j++) {
                if (nums[j] < nums[minIdx]) {
                    minIdx = j;
                }
            }
            swap(nums[i], nums[minIdx]);
        }
        return nums;
    }
};