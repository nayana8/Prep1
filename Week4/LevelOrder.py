# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        if A == None:
            return []
            
        q = []
        q1 = []
        q.append(A)
        res = []
        res.append([A.val])
        while len(q) != 0:
            temp = q.pop(0)
            if temp and temp.left:
                q1.append(temp.left)
            if temp and temp.right:
                q1.append(temp.right)
            if len(q) == 0:
                t = []
                for node in q1:
                    t.append(node.val)
                res.append(t)
                q, q1 = q1, None
        return res
                