class Solution(object):
    def canMerge(self, trees):
        nodes = {}
        indegree = {}
        
        for t in trees:
            nodes[t.val] = t
            indegree[t.val] = indegree.get(t.val, 0)
            if t.left:
                indegree[t.left.val] = indegree.get(t.left.val, 0) + 1
            if t.right:
                indegree[t.right.val] = indegree.get(t.right.val, 0) + 1
                
        root = None
        for t in trees:
            if indegree[t.val] == 0:
                if root:
                    return None
                root = t
                
        if not root:
            return None
            
        count = [0]
        
        def traverse(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
                
            if not node.left and not node.right:
                if node.val in nodes and node != nodes[node.val]:
                    child = nodes[node.val]
                    node.left = child.left
                    node.right = child.right
                    del nodes[node.val]
                    
            count[0] += 1
            return traverse(node.left, low, node.val) and traverse(node.right, node.val, high)
            
        del nodes[root.val]
        if not traverse(root, float('-inf'), float('inf')):
            return None
            
        return root if len(nodes) == 0 and count[0] == sum(1 + (1 if t.left else 0) + (1 if t.right else 0) for t in trees) - (len(trees) - 1) else None
