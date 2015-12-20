#!/bin/python

import sys

cards = []

cards_i = 0
for cards_i in xrange(5):
    cards_t = str(raw_input().strip())
    cards.append(cards_t)

suits = ["S", "H", "D", "C"]


def build_map_big():
    map = {}
    for i in range(2, 11):
        map[str(i)] = i
    map["A"] = 1
    map["T"] = 10
    map["J"] = 11
    map["Q"] = 12
    map["K"] = 13
    return map


def build_map_small():
    map = {}
    for i in range(2, 11):
        map[str(i)] = i
    map["T"] = 10
    map["J"] = 11
    map["Q"] = 12
    map["K"] = 13
    map["A"] = 14
    return map


def is_straight_flush(cards):
    start = cards[0][0]
    end = cards[4][0]
    suit_start = cards[0][1]
    suit_end = cards[4][1]
    if suit_start in suits or suit_end in suits:
        if start == "A":
            map = build_map_small()
            for i in range(1, len(cards)):
                if cards[i][1] != suit_start:
                    return "NO"
                if map[cards[i][0]] == map[cards[i-1][0]]+1:
                    pass
                else:
                    return "NO"
            return "YES"
        elif end == "A":
            map = build_map_big()
            for i in reversed(range(0, len(cards)-1)):
                if cards[i][1] != suit_end:
                    return "NO"
                if map[cards[i][0]] == map[cards[i+1][0]]-1:
                    pass
                else:
                    return "NO"
            return "YES"
        else:
            map = build_map_big()
            for i in range(1, len(cards)):
                if cards[i][1] != suit_start:
                    return "NO"
                print map[cards[i][0]]
                if map[cards[i][0]] == map[cards[i-1][0]]+1:
                    pass
                else:
                    print "??"
                    return "NO"
            return "YES"

print(is_straight_flush(cards))
