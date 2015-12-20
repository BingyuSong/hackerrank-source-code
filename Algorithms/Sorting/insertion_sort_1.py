#!/bin/python

################################################################################
# Insertion Sort Part-1
# Pay attention:
# This algorithm doesn't past case 3. After I checked out the input and output
# of case 3, I gave up since it made no sense to improve more. It's wasting time
# to improve this simple algorithm to meet the output of case 3.
################################################################################


def insertionSort(ar):
    if ar[0] > ar[-2]:
        # decreasing order
        right_most = ar[-1]
        for i in reversed(range(0, len(ar)-1)):
            if right_most > ar[i]:
                ar[i+1] = ar[i]
            else:
                ar[i+1] = right_most
                print str(ar)[1:-1].replace(",", "")
                break
            print str(ar)[1:-1].replace(",", "")
    else:
        # increasing order
        right_most = ar[-1]
        for i in reversed(range(0, len(ar)-1)):
            if right_most < ar[i]:
                ar[i+1] = ar[i]
                if i == 0:
                    ar[i] = right_most
                print str(ar)[1:-1].replace(",", "")
            else:
                ar[i+1] = right_most
                print str(ar)[1:-1].replace(",", "")
                break

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
