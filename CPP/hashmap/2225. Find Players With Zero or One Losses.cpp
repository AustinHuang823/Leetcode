class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> loss_count;
        for (vector<int> match: matches){
            int winner = match[0], loser = match[1];
            if (loss_count.find(winner) == loss_count.end()){
                loss_count[winner] = 0;
            }
            loss_count[loser]++;
        }
        vector<vector<int>> res(2,vector<int>());
        for (auto [player, loss]: loss_count){
            if (loss == 0) res[0].push_back(player);
            else if (loss == 1) res[1].push_back(player);
        }
        sort(res[0].begin(), res[0].end());
        sort(res[1].begin(), res[1].end());
        return res;
        // unordered_map<int, int> loss_count;
        // set<int> players;
        // for (vector<int> match: matches){
        //     players.insert(match[0]);
        //     players.insert(match[1]);
        //     loss_count[match[1]]++;
        // }
        // vector<vector<int>> res;
        // vector<int> one_loss, zero_loss;
        // for (int p: players){
        //     if (loss_count[p] == 0) zero_loss.push_back(p);
        //     else if (loss_count[p] == 1) one_loss.push_back(p);
        // }
        // res.push_back(zero_loss);
        // res.push_back(one_loss);
        // return res;
    }
};