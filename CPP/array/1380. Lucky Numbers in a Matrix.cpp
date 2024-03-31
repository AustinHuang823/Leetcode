class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> res;
        for (int i = 0; i < matrix.size(); i++){
            int minIdx, j, minVal = INT_MAX;
            for (j = 0; j < matrix[i].size(); j++){
                if (matrix[i][j] < minVal){
                    minIdx = j;
                    minVal = matrix[i][j];
                }
            }
            for (j = 0; j < matrix.size(); j++){
                if (j == i) continue;
                if (matrix[j][minIdx] > minVal) break;
            }
            if (j == matrix.size()) res.push_back(minVal);
        }   
        return res;
    }
};