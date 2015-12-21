#!/usr/bin/env python
# -*- coding: utf-8 -*-


################################################################################
# Pangrams
################################################################################

letters = set()
s = raw_input()

for i in range(0, len(s)):
    if 65<=ord(s[i])<=90:
        # can user s[i].lower() instead.
        letters.add(chr(ord(s[i])+32))
    elif 97<=ord(s[i])<=122:
        letters.add(s[i])
    else:
        pass

if len(letters) == 26:
    print "pangram"
else:
    print "not pangram"
