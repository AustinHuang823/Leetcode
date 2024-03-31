class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (auto& n: nums){
            counter[n]++;
        }
        auto cmp = [](pair<int, int>& a, pair<int, int>& b){
            return a.second > b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        for (auto& n: counter){
            pq.push(n);
            if (pq.size()>k){
                pq.pop();
            } 
        }
        vector<int> res;
        while (!pq.empty()){
            res.push_back(pq.top().first);
            pq.pop();
        }
        return res;
    }
};