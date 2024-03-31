/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    long long kthLargestLevelSum(TreeNode* root, int k) {
        priority_queue<long long, vector<long long>, greater<long long>> pq;
        queue<TreeNode*> q;
        long long lvl_sum = 0;
        q.push(root);
        while (!q.empty()){
            int n = q.size();
            for (int i = 0; i < n; i++){
                TreeNode* cur_node = q.front();
                q.pop();
                lvl_sum += cur_node->val;
                if (cur_node->left != nullptr) q.push(cur_node->left);
                if (cur_node->right != nullptr) q.push(cur_node->right);
            }
            pq.push(lvl_sum);
            if (pq.size() > k) pq.pop();
            lvl_sum = 0;
        }
        if (pq.size() < k) return -1;
        return pq.top();
    }
};