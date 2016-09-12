#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):

    def canWinNim(self, n):
        if n % 4 == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    print s.canWinNim(5)
