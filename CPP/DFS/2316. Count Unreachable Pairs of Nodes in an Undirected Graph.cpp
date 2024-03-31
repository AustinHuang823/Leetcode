class Solution {
public:
    void dfs(int node, unordered_map<int, vector<int>>& m,long long& count, vector<int>& visited){
        visited[node] = 1;
        count++;
        for (int& i: m[node]){
            if (visited[i] == 0){
                dfs(i, m, count, visited);
            }
        }
    }
    
    long long countPairs(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> m;
        for (int i = 0; i < edges.size(); i++){
            m[edges[i][0]].push_back(edges[i][1]);
            m[edges[i][1]].push_back(edges[i][0]);
        }
        long long res = ((long long)n*(n-1))/2;
        vector<int> visited(n,0);
        long long count;
        for (int i = 0; i < n; i++){
            if (visited[i] == 1){
                continue;
            }
            count = 0;
            dfs(i, m, count, visited);
            res -= (count*(count-1))/2;
        }
        return res;
    }


};