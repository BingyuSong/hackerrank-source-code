#!/usr/bin/env python
# -*- coding: utf-8 -*-

def intersect(nums1, nums2):
    dict1 = {}
    interset = []

    if (len(nums1) == 0 or len(nums2) == 0):
        return []
    for ele in nums1:
        if dict1.get(ele):
            pass
        else:
            dict1[ele] = 1

    for e in nums2:
        try:
            if dict1[e]:
                interset.append(e)
                dict1[e] -= 1
        except:
            pass
    return interset


if  __name__ == "__main__":
    a1 = [1,2]
    a2 = [1,1]

    print intersect(a1, a2)
