/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution
{
    public:

        int acc = 0; // counter

        void sumTree(TreeNode* root, int L, int R)
        {
            if(!root) return;

            if(root->val >= L && root->val <= R)
            {
                acc += root->val;
            }
            sumTree(root->left,L,R);
            sumTree(root->right,L,R);
        }

        int rangeSumBST(TreeNode* root, int L, int R)
        {
            sumTree(root,L,R);
            return acc;
        }
};