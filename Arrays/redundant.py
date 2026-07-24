class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = {}
        candidate1 = None
        candidate2 = None

        for u, v in edges:
            if v in parent:
                candidate1 = parent[v]
                candidate2 = [u, v]
                break
            parent[v] = [u, v]

        def find(node, roots):
            if roots[node] == node:
                return node
            roots[node] = find(roots[node], roots)
            return roots[node]

        def union(node1, node2, roots):
            root1 = find(node1, roots)
            root2 = find(node2, roots)
            if root1 == root2:
                return False
            roots[root1] = root2
            return True

        roots = list(range(n + 1))
        for u, v in edges:
            if [u, v] == candidate2:
                continue
            if not union(u, v, roots):
                if candidate1:
                    return candidate1
                return [u, v]

        return candidate2
