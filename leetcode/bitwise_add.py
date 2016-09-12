#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def getSum(self, a, b):
        if abs(a) == abs(b):
            return 0
        while a:
            c = b & a
            d = b ^ a
            a = c << 1
            b = d
        return b


if __name__ == "__main__":
    s = Solution()
    print s.getSum(14, -16)
