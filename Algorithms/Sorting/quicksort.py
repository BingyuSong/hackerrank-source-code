#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Quicksort (uncompleted)
# URL: https://www.hackerrank.com/challenges/quicksort2
################################################################################
def partition(arr, low, high):
    pivot = arr[low]
    j = low+1
    for i in range(low+1, high):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[low], arr[j-1] = arr[j-1], arr[low]
    return j-1

def quick_sort(arr, low, high):
    if low<high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p+1, high)



m = int(raw_input())
arr = [int(i) for i in raw_input().strip().split()]
quick_sort(arr, 0, m)
print str(arr)[1:-1].replace(",", "")
