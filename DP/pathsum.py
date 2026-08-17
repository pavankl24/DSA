class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def gain_from_sub_tree(node):
            if not node:
                return 0
            
            left_gain = max(gain_from_sub_tree(node.left), 0)
            right_gain = max(gain_from_sub_tree(node.right), 0)
            
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)
            
            return node.val + max(left_gain, right_gain)
        
        gain_from_sub_tree(root)
        return self.max_sum
