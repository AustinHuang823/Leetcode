
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cur_min_cost = -INT_MAX;
        int profit = 0;
        for (int n: prices){
            if (-n > cur_min_cost){
                cur_min_cost = -n;
                continue;
            }
            if (profit < n + cur_min_cost){
                profit = n + cur_min_cost;
            }
        }
        return profit;
    }
};