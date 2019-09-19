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

        TreeNode* insertIntoBST(TreeNode* root, int val)
        {
            if(val < root->val)
            {
                if(root->left == NULL)
                {
                    root->left = new TreeNode(val);
                }
                else
                {
                    insertIntoBST(root->left, val);
                }
            }

            if(val > root->val)
            {
                if(root->right == NULL)
                {
                    root->right = new TreeNode(val);
                }
                else
                {
                    insertIntoBST(root->right, val);
                }
            }

            return root;
        }
};