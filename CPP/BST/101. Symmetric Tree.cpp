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
    bool isSymmetric(TreeNode* root) {
        if (root->left && root->right){
            return helper(root->left, root->right);
        }
        else if (root->left == nullptr && root->right == nullptr){
            return true;
        }
        return false;
    }

    bool helper(TreeNode* r1, TreeNode* r2){
        if (r1) cout << "r1:" << r1->val;
        if (r2) cout << "r2:" << r2->val << endl;
        if (r1 == nullptr && r2 == nullptr) {
            return true;
        }
        else if (r1 && r2){
            if (r1->val == r2->val) {
                if (helper(r1->left, r2->right) && helper(r1->right, r2->left)){
                    return true;
                }
            }
        }
        return false;
    }
};