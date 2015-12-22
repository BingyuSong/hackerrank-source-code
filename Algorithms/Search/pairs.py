#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Pairs
# URL: https://www.hackerrank.com/challenges/pairs
# It didn't pass some cases due to timeout.
################################################################################


def pairs_one(a, k):        # O(nlogn)
    answer = 0
    a = sorted(a)    # Timesort -> worst case: O(nlogn).
    for i in range(0, len(a)):  # O(n)
        if a[i]+k in a:
            answer += 1
        if a[i]+k > a[-1]:
            break
    return answer


def pairs_two(a, k):
    '''This algorithm obtains O(n) using hash table, really good implementation!
    Reference:
        https://github.com/duaraghav8/Hackerrank-Problems/blob/master/pairs.py
    '''
    answer = 0
    hash_table = {int(i): 1 for i in a}
    for num in hash_table:
        try:
            t = hash_table[num+k]
        except:
            continue
        answer += 1
    return answer

[count, distance] = [int(i) for i in raw_input().strip().split()]
a = [int(i) for i in raw_input().strip().split()]
print(pairs_two(a, distance))
