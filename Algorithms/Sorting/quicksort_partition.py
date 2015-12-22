#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Quicksort 1 - Partition
# URL:https://www.hackerrank.com/challenges/quicksort1
################################################################################


def hoare_partition(arr, m):
    pass


def lomuto_partition(arr, m):
    pivot = arr[0]
    j = 1
    for i in range(1, m):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[0], arr[j-1] = arr[j-1], arr[0]
    print str(arr)[1:-1].replace(",", "")


m = int(raw_input())
arr = [int(i) for i in raw_input().strip().split()]
lomuto_partition(arr, m)
