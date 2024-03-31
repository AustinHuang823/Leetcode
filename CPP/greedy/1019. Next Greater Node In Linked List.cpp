/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> res;
        stack<int> s;
        while (head != nullptr){
            res.push_back(head->val);
            head = head->next;
        }
        for (int i = res.size()-1; i >=0; --i){
            int curr_val = res[i];
            while(!s.empty() && s.top() <= curr_val) s.pop();
            res[i] = s.empty() ? 0: s.top();
            s.push(curr_val);
        }
        return res;
    }
};