#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):

    def singleNumber(self, nums):
        h = {}
        for ele in nums:
            if ele in h.keys():
                h.pop(ele)
            else:
                h[ele] = 1
        return h.keys()[0]


if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([1,1,2,3,3,4,4])
