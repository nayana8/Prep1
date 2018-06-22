# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if node == None:
            return None
        
        visited = {}
        h = {}
        q = []
        q.append(node)
        g = None
        while len(q) > 0:
            n = q.pop(0)
            
            if n in visited:
                continue
            
            visited[n] = True
            if n.label in h:
                new = h[n.label]
            else:
                new = UndirectedGraphNode(n.label)
                h[n.label] = new
                
            if g == None:
                g = new
            #print new.label
            for neigh in n.neighbors:
                if neigh.label in h:
                    child = h[neigh.label]
                else:
                    child = UndirectedGraphNode(neigh.label)
                    h[neigh.label] = child
                #print new.label, child.label
                new.neighbors.append(child)
                q.append(neigh)
        return g