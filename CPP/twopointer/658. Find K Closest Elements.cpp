class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> temp;
        for (int n: arr){
            temp.push_back(abs(n - x));
        }
        int l = 0;
        int r = temp.size()-1;
        while ((r-l+1) > k){
            if (temp[r] >= temp[l]) r--;
            else l ++;
        }
        return vector<int>(arr.begin() + l, arr.begin() + r + 1);
    }
};