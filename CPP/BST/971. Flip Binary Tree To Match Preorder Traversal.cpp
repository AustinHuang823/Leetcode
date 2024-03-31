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
vector<int> flips;
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
        int pos = 0;
        if (fliptree(root, voyage, pos)) return flips;
        return {-1};
    }
    bool fliptree(TreeNode* root, vector<int>& voyage, int& pos){
        if (root == nullptr) return true;
        if (root->val != voyage[pos]) return false;
        pos++;
        if (root->left != nullptr && root->left->val != voyage[pos]){
          flips.push_back(root->val);
          swap(root->left, root->right);
        }
        return fliptree(root->left, voyage, pos) && fliptree(root->right, voyage, pos);
    }
};

