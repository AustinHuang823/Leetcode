class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        long long ans = 0;
        
        priority_queue<int, vector<int>, greater<int>> pq_left, pq_right;

        int cnt = 0;
        int l = 0;
        int r = costs.size()-1;

        while (cnt<k){
            while(pq_left.size() < candidates && l <= r) pq_left.push(costs[l++]);
            while(pq_right.size() < candidates && r >= l) pq_right.push(costs[r--]);
            int cost_left = pq_left.size() > 0 ? pq_left.top(): INT_MAX;
            int cost_right = pq_right.size() > 0 ? pq_right.top(): INT_MAX;

            if (cost_left <= cost_right){
                ans += cost_left;
                pq_left.pop();
            }
            else{
                ans += cost_right;
                pq_right.pop();
            }

            cnt++;

        }
        return ans;
    }
};