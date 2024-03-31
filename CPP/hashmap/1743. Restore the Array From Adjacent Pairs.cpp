class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, int> Counter;
        unordered_map<int, vector<int>> edges;
        for (vector<int> v: adjacentPairs){
            Counter[v[0]]++;
            Counter[v[1]]++;
            edges[v[0]].push_back(v[1]);
            edges[v[1]].push_back(v[0]);
        }
        vector<int> res;
        int curr;
        for (pair<int, int> p: Counter){
            if (p.second == 1) {
                curr = p.first;
                --Counter[curr];
                res.push_back(curr);
                curr = edges[curr][0];
                --Counter[curr];
                res.push_back(curr);
                break;
            }
        }
        while (Counter[curr] != 0){
            for (int next: edges[curr]){
                if (Counter[next] != 0){
                    --Counter[curr];
                    curr = next;
                    res.push_back(curr);
                    --Counter[curr];
                }
            }
        }
        return res;
        // while (res.size() < adjacentPairs.size() + 1){
        //     for (vector<int> v: adjacentPairs){
        //         if (v[0] == curr && Counter[v[1]] != 0){
        //             curr = v[1];
        //             Counter[curr] = 0;
        //             res.push_back(curr);
        //             break;
        //         }
        //         else if (v[1] == curr && Counter[v[0]] != 0){
        //             curr = v[0];
        //             Counter[curr] = 0;
        //             res.push_back(curr);
        //             break;
        //         }
        //     }
        // }

        // return res;
    }
};