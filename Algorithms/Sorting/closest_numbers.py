#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Closest Numbers
# URL: https://www.hackerrank.com/challenges/closest-numbers
# Test Case #4: Time out
################################################################################


def closest_numbers(arr):
    closest_distance = 99999
    closest_distance_pair = []
    length = len(arr)
    for i in range(0, length):
        for j in range(i+1, length):
            distance = abs(arr[i] - arr[j])
            if distance < closest_distance:
                closest_distance = distance
                closest_distance_pair = []
                closest_distance_pair += [arr[i], arr[j]]
            elif distance == closest_distance:
                closest_distance_pair += [arr[i], arr[j]]
    print str(sorted(closest_distance_pair))[1:-1].replace(",", "")


m = int(raw_input())
arr = [int(i) for i in raw_input().strip().split()]
closest_numbers(arr)
