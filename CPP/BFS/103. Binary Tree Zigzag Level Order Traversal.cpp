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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        deque<TreeNode*> dq;
        if (root != nullptr) dq.push_back(root);
        int curlvl = 0, i;
        vector<int> thislvl;
        vector<vector<int>> res;
        while(!dq.empty()){
            int it = dq.size();
            if (curlvl % 2 == 0){
                for (i = 0; i < it; i++){
                TreeNode* node = dq.front();
                dq.pop_front();
                thislvl.push_back(node->val);
                if (node->left != nullptr) dq.push_back(node->left);
                if (node->right != nullptr) dq.push_back(node->right);
                }
            }
            else{
                for (i = 0; i < it; i++){
                TreeNode* node = dq.back();
                dq.pop_back();
                thislvl.push_back(node->val);
                if (node->right != nullptr) dq.push_front(node->right);
                if (node->left != nullptr) dq.push_front(node->left);
                }
            }
            res.push_back(thislvl);
            thislvl.clear();
            curlvl++;
        }
        return res;
    }
};