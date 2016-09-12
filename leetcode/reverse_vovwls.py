#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):

    def reverseVowels(self, s):
        length = len(s)
        l = list(s)
        if (not length) or (length == 1):
            return s
        end = length - 1
        start = 0

        vovwls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while start < end:
            if (l[start] in vovwls) and (l[end] in vovwls):
                l[start], l[end] = l[end], l[start]
                start +=1
                end -= 1
            elif l[start] in vovwls:
                end -= 1
            elif l[end] in vovwls:
                start += 1
            else:
                start +=1
                end -= 1

        return "".join(l)



if __name__ == "__main__":
    s = Solution()
    print s.reverseVowels("hellO")
