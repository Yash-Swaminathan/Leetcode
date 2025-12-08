# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Return True if Height returns non-negative (balanced), False if -1 (imbalanced)
        return (self.Height(root) >= 0)
    
    def Height(self, root):
        # Base case: empty tree has height 0
        if root is None:
            return 0
        
        # Recursively get heights of left and right subtrees
        left, right = self.Height(root.left), self.Height(root.right)
        
        # Check if tree is imbalanced:
        # - left < 0: left subtree is imbalanced
        # - right < 0: right subtree is imbalanced
        # - abs(left - right) > 1: current node has height difference > 1
        if left < 0 or right < 0 or abs(left - right) > 1:  
            return -1  # Return -1 to signal imbalance
        
        # Tree is balanced, return actual height (max of subtrees + 1)
        return max(left, right) + 1