class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int target = graph.size()-1;
        vector<vector<int>> res;
        
        dfs(graph, 0, {}, target, res);
        return res;
    }

    void dfs(vector<vector<int>>& graph, int pos, vector<int> path, int& target, vector<vector<int>>& res){
        path.push_back(pos);
        if(pos == target){
            res.push_back(path);
        }
        else{
            for (int next_pos: graph[pos]){
                dfs(graph, next_pos, path, target, res);
            }
        }
        return;
    }
};