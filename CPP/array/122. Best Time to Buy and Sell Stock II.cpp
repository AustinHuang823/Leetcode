class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int cur_cost = -INT_MAX;
        int prev_profit = 0;
        for (int price: prices){
            if (price + cur_cost < prev_profit){
                profit += prev_profit;
                prev_profit = 0;
                cur_cost = -price;
            }
            else if (-price > cur_cost){
                cur_cost = -price;
            }
            else if (price + cur_cost > prev_profit){
                prev_profit = price + cur_cost;
            }
            // cout << "cur price:" << price << ", profit:" << profit << ", cur_cost:" << cur_cost << ", prev_profit:" << prev_profit << endl;
        }
        profit += prev_profit;
        return profit;
    }
};