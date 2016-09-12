#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def findTheDifference(self, s, t):
        d = {}
        for c in t:
            if d.get(c):
                d[c] += 1
            else:
                d[c] = 1
        for c in s:
            if d.get(c):
                d[c] -= 1
                if d[c] == 0:
                    d.pop(c)
            else:
                return c
        return d.keys()[0]


if __name__ == "__main__":
    s = Solution()
    print s.findTheDifference("abced", "abcedf")
