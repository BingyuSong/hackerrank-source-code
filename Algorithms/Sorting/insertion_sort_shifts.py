#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Running Time of Algorithms
# Ulr: https://www.hackerrank.com/challenges/runningtime/submissions/code/15904487
################################################################################


def compute_shifts(arr):
    shift_count = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                shift_count += 1
            j -= 1
    return shift_count


m = int(raw_input())
arr = [int(i) for i in raw_input().strip().split()]
print(compute_shifts(arr))
