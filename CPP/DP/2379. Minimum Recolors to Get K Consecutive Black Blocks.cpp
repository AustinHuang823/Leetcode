class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int minVal = 0;
        for (int i = 0; i < k; i++){
            if (blocks[i] == 'W') minVal++;
        }
        int curVal = minVal;
        for (int i = k; i < blocks.size(); i++){
            if (blocks[i] == 'W') curVal++;
            if (blocks[i-k] == 'W') curVal--;
            if (curVal < minVal) minVal = curVal;
        }
        return minVal;
    }
};