#include <vector>
#include <iostream>
#include <climits>
using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int r = m+n-1;
    m--;
    n--;
    while (r >= 0){
        if (m < 0){
            nums1[r] = nums2[n];
            n--;
            }
        else if (n < 0){
            nums1[r] = nums1[m];
            m--;
        }
        else if (nums1[m] > nums2[n]){
            nums1[r] = nums1[m];
            m--;
        }
        else{
            nums1[r] = nums2[n];
            n--;
        }
        r--;
    }
    for (auto & n: nums1){
        cout << n;
    }
    cout << endl;
}

int main(){
    // vector<int> nums1 = {1,2,3,0,0,0};
    // int m = 3;
    // vector<int> nums2 = {4,5,6};
    // int n = 3;
    // merge(nums1, m, nums2, n);
    float x;
    x = 3./4;
    cout << x<< endl;
    return 0;
}