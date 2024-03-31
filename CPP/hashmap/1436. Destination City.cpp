class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_map<string, string> edges;
        for (vector<string> path: paths){
            edges[path[0]] = path[1];
        }
        string curr = paths[0][0];
        while (edges.count(curr) != 0){
            curr = edges[curr];
        }

        return curr;
    }
};