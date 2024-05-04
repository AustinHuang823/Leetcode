#include <vector>
#include <algorithm>

using namespace std;

/*
Runtime: 485 beat 26%
Memory: 68.96 beat 95%
Time: nlogn
Space: logn (depth of recursion)
*/

class Solution {
public:
    void quickSort(vector<int>& nums, int left, int right) {
        if (left >= right) return;
        int pivot = nums[left + (right - left) / 2];
        int l = left, r = right;
        while (l <= r) {
            while (nums[l] < pivot) l++;
            while (nums[r] > pivot) r--;
            if (l <= r){
                swap(nums[l], nums[r]);
                l++;
                r--;
            }
        }
        quickSort(nums, left, r);
        quickSort(nums, l, right);
    }
    
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }
};