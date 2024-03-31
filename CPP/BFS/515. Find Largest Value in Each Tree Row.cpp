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
    vector<int> largestValues(TreeNode* root) {
        int curMax = INT_MIN;
        queue<TreeNode*> q;
        if (root != nullptr) q.push(root);
        vector<int> res;
        while(!q.empty()){
            int n = q.size();
            for (int i = 0; i < n; i++){
                TreeNode* curNode = q.front();
                q.pop();
                curMax = max(curNode->val, curMax);
                if (curNode->left != nullptr) q.push(curNode->left);
                if (curNode->right != nullptr) q.push(curNode->right);
            }
            res.push_back(curMax);
            curMax = INT_MIN;
        }
        return res;
    }
};