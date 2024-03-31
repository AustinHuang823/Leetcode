class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int maj_ele;

        for (int n: nums){
            if (count == 0){
                maj_ele = n;
                count++;
            }
            else if (maj_ele == n) count++;
            else count--;
        }
        return maj_ele;
    }
};