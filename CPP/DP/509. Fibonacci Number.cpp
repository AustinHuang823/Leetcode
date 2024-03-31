class Solution {
public:
    int fib(int n) {
        vector<int> fibvec = {0, 1};
        if (n == 0) return fibvec[0];
        for (int i = 1; i < n; i++){
            int v0 = fibvec[0];
            fibvec[0] = fibvec[1];
            fibvec[1] = fibvec[1] + v0;
        }
        return fibvec[1];
    }
};