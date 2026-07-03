class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
            
        cloned_nodes = {}
        
        def dfs(curr_node):
            if curr_node in cloned_nodes:
                return cloned_nodes[curr_node]
                
            copy = Node(curr_node.val)
            cloned_nodes[curr_node] = copy
            
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)
