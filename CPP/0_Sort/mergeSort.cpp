#include <vector>
using namespace std;

/*
Time: nlogn
Space: n
*/

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size()-1);
        return nums;
    }

    void mergeSort(vector<int>& vec, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSort(vec, l, m);
            mergeSort(vec, m+1, r);
            merge(vec, l, m, r);
        }
    }

    void merge(vector<int>& vec, int l, int m, int r) {
        vector<int> lSub(vec.begin() + l, vec.begin() + m + 1);
        vector<int> rSub(vec.begin() + m + 1, vec.begin() + r + 1);
        
        int lIdx = 0, rIdx = 0, vecIdx = l;
        while (lIdx < lSub.size() && rIdx < rSub.size()) {
            if (lSub[lIdx] < rSub[rIdx]) {
                vec[vecIdx] = lSub[lIdx];
                lIdx++;
            }
            else {
                vec[vecIdx] = rSub[rIdx];
                rIdx++;
            }
            vecIdx++;
        }
        while (lIdx < lSub.size()) {
            vec[vecIdx] = lSub[lIdx];
            lIdx++;
            vecIdx++;
        }
        while (rIdx < rSub.size()) {
            vec[vecIdx] = rSub[rIdx];
            rIdx++;
            vecIdx++;
        }
    }
};