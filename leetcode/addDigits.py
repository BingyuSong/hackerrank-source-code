#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def addDigits(self, num):
        l = [1,2,3,4,5,6,7,8,9]
        if num < 10:
            return num
        a = num % 9
        return l[a-1]

if __name__ == "__main__":
    s = Solution()
    print s.addDigits(12345)
