class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int cur_c = capacity;
        int steps = 0;
        for (int i=0; i<plants.size(); i++){
            if (cur_c >= plants[i]){
                cur_c -= plants[i];
                steps += 1;
            }
            else{
                steps += (i + 1) * 2 - 1;
                cur_c = capacity - plants[i];
            }
        }
        return steps;
    }
};