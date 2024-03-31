class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest = 0, curr = 0;
        int n = gain.size();
        // int curr = 0;
        // std::cout << n << std::endl;
        for (int i = 0; i < n; i++){
            curr += gain[i];
            highest = max(highest, curr);
        }
        return highest;
    }
};