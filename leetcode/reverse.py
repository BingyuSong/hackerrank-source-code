#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class Solution(object):

    def reverseString(self, s):
        start_time = time.time()
        length = len(s)
        s_r = []
        if (not length) or (length == 1):
            return s
        last_index = length - 1
        while last_index >= 0:
            s_r.append(s[last_index])
            last_index -= 1
        print "time is %s" % (time.time() - start_time)
        return "".join(s_r)


if __name__ == "__main__":
    s = Solution()
    print s.reverseString("a bb cc , efa        ")
