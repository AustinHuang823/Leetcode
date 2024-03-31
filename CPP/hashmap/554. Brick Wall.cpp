#include <iostream>
#include <vector>
#include <unordered_map>
#include <numeric>
using namespace std;

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int m = accumulate(wall[0].begin(), wall[0].end(), 0);
        unordered_map<int, int> passing_map;
        int temp = 0;
        for (vector<int> bricks: wall){
            for (int brick: bricks){
                temp += brick;
                passing_map[temp]++;
            }
            temp = 0;
        }
        passing_map[m] = 0;
        int n = wall.size();
        int max_pass = INT_MIN;
        for (pair<int, int> p: passing_map){
            cout << p.first << p.second << endl;
            if (p.second > max_pass) max_pass = p.second;
        }
        return n-max_pass;
    }
};

int main() {
    Solution s;
    vector<vector<int>> wall = {{1,2,2,1},
                                {3,1,2},
                                {1,3,2},
                                {2,4},
                                {3,1,2},
                                {1,3,1,1}};
    cout << s.leastBricks(wall) << endl;
    return 0;
}