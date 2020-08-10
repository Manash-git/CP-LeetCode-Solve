class TreeNode:
    pass
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root.val > target and root.left != None: 
            l = self.closestValue(root.left, target)
            if abs(l-target) < abs(root.val-target):
                return l
            
            return root.val
        
        if root.val < target and root.right != None: 
            r = self.closestValue(root.right, target)
            if abs(r-target) < abs(root.val-target):
                return r
            return root.val
        
        return root.val 