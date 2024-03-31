class Solution {
public:
    int climbStairs(int n) {
        if (n<=2) return n;
        vector<int> last3 = {0,1,2};
        for (int i = 2; i < n; i++){
            last3[0] = last3[1];
            last3[1] = last3[2];
            last3[2] = last3[0]+last3[1];
        }
        return last3[2];
    }
};