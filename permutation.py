#! /usr/bin/env python

import numpy.random as rd

########################################
# non-destractive permutation
# using additional O(n) space
########################################
def permuate(a, p):
    return [ a[ p[i] ] for i in xrange( len(a) ) ]


########################################
# destractive permutation
# assumming sizeof(a[i]) = sizeof(p[i])
# by beam2d
########################################
def permutate_beam2d(a, p):
    for i in xrange(len(a)):
        t, p[i] = p[i], a[i]           # escape p[i] -> t and a[i] -> p[i]
        a[i] = a[t] if t > i else p[t] # change a[i] to (escaped) target value


########################################
# destractive permutation
# using additional n log n bits
# by Darsein
########################################
def permutate_Darsein(a, p):
    n = len(a)

    # permutate a
    for i in xrange(n):
        # permuate cycle starting with i
        j = i
        while p[j] < n:
            k = p[j]     # next point
            if k != i: a[j], a[k] = a[k], a[j] # swap if not starting point
            p[j] = k + n # mark as visited
            j = k        # move to next

    # recover p
    for i in xrange(n):
        p[i] -= n


########################################
# main
########################################
if __name__ == '__main__':
    N = 10

    # target array
    a = range(N)

    # permutation
    p = range(N)
    rd.shuffle(p)

    # permutate a by p
    print "a =", a
    print "p =", p

    print "parmutate!!"
    permutate_beam2d(a, p)

    print "a =", a
    print "p =", p
