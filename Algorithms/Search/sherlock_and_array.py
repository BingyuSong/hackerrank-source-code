#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Sherlock and Array
# URL: https://www.hackerrank.com/challenges/sherlock-and-array
# It didn't pass test case #3 and test case #4 due to timeout.
################################################################################

MAX = 10*10*10*10

def sherlock_array(seq):
    if len(seq) == 1:
        return "YES"
    if len(seq) < 1:
        return "NO"
    sum_list = [seq[0]]
    sum_list_reverse = [seq[-1]]
    revser_i = -2
    for i in range(1, len(seq)):
        sum_list.append(sum_list[-1]+seq[i])
        sum_list_reverse.insert(0, sum_list_reverse[0]+seq[revser_i])
        revser_i -= 1
    for i in range(1, len(seq) - 1):
        if sum_list[i] == sum_list_reverse[i]:
            return "YES"
    return "NO"


if __name__ == "__main__":
    T = int(raw_input())
    result = []
    if 1 <= T <= 10:
        for i in range(T):
            seq = []
            N = int(raw_input())
            if 1 <= N <= MAX*10:
                seq = [int(i) for i in raw_input().strip().split(" ")]
                result.append(sherlock_array(seq))
    for p in result:
        print p
