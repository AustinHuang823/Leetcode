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
    bool SameTree(TreeNode* r1, TreeNode* r2){
        queue<TreeNode*> q1;
        queue<TreeNode*> q2;
        q1.push(r1);
        q2.push(r2);
        while (!q1.empty() && !q2.empty()){
            TreeNode* n1 = q1.front();
            TreeNode* n2 = q2.front();            
            q1.pop();
            q2.pop();
            if (n1 == nullptr && n2 == nullptr) continue;
            else if (n1 == nullptr || n2 == nullptr) return false;
            else if (n1->val != n2->val) return false;
            q1.push(n1->left);
            q2.push(n2->left);
            q1.push(n1->right);
            q2.push(n2->right);
        }
        return q1.empty() && q2.empty() ? true: false;
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        vector<TreeNode*> possible_roots;
        queue<TreeNode*> q;
        q.push(root);
        int target = subRoot->val;
        while (!q.empty()){
            TreeNode* node = q.front();
            q.pop();
            if (node->val == target){
                possible_roots.push_back(node);
            }
            if (node->left != nullptr) q.push(node->left);
            if (node->right != nullptr) q.push(node->right);
        }
        for (auto& node: possible_roots){
            if (SameTree(node, subRoot)) return true;
        }
        return false;
    }
};