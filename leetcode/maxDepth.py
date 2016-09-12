#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, root):
        if not root:
            return 0
        elif not root.left:
            return self.maxDepth(root.right) + 1
        elif not root.right:
            return self.maxDepth(root.left) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    s = Solution()
