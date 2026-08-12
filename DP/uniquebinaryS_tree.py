class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
            
        def build_trees(start, end):
            if start > end:
                return [None]
                
            all_trees = []
            for i in range(start, end + 1):
                left_subtrees = build_trees(start, i - 1)
                right_subtrees = build_trees(i + 1, end)
                
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            return all_trees
            
        return build_trees(1, n)
