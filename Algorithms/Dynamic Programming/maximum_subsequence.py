#!/usr/bin/env python
# -*- coding: utf-8 -*-

MAX = 10*10*10*10


def max_continuous_subsequence(list, length):
    start_index = 0
    best_start_index = -1
    best_end_index = -1
    best_sum = 0
    current_sum = 0
    for i in range(length):
        val = current_sum + list[i]
        if val > 0:
            if current_sum == 0:
                start_index = i
            current_sum = val
        else:
            current_sum = 0
        if current_sum > best_sum:
            best_sum = current_sum
            best_start_index = start_index
            best_end_index = i

    return sum(list[best_start_index:best_end_index+1])


def max_subsequence(list, length):
    all_ng = False
    s = sum([i for i in list if i > 0])
    if s == 0 and length != 0:
        all_ng = True
        return max(list), all_ng
    return s, all_ng


T = int(raw_input())
result = []
if 1 <= T <= 10:
    for i in range(T):
        solution = []
        N = int(raw_input())
        if 1 <= N <= MAX*10:
            seq = [int(i) for i in raw_input().strip().split(" ")]
            no_con_sum, all_ng = max_subsequence(seq, N)
            if all_ng:
                solution = [no_con_sum, no_con_sum]
            else:
                solution = [max_continuous_subsequence(seq, N), max_subsequence(seq, N)[0]]
        result.append(solution)

for p in result:
    print str(p)[1:-1].replace(",", "")

