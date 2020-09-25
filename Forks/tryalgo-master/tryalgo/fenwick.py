#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Fenwick tree
jill-jenn vie et christoph durr - 2014-2018
"""


# snip{
class Fenwick:
    """maintains a tree to allow quick updates and queries
    """
    def __init__(self, t):
        """stores a table t and allows updates and queries
        of prefix sums in logarithmic time.

        :param array t: with numerical values
        """
        self.s = [0] * (len(t) + 1)  # create internal storage
        for a in range(len(t)):
            self.add(a, t[a])        # initialize

    # pylint: disable=redefined-builtin
    def prefixSum(self, a):
        """
        :param int a: index in t, negative a will return 0
        :returns: t[0] + ... + t[a]
        """
        i = a + 1                  # internal index starts at 1
        total = 0
        while i > 0:               # loops over neighbors
            total += self.s[i]     # cumulative sum
            i -= (i & -i)          # left neighbor
        return total

    def intervalSum(self, a, b):
        """
        :param int a b: with 0 <= a <= b
        :returns: t[a] + ... + t[b]
        """
        return self.prefixSum(b) - self.prefixSum(a-1)

    def add(self, a, val):
        """
        :param int a: index in t
        :modifies: adds val to t[a]
        """
        i = a + 1                  # internal index starts at 1
        while i < len(self.s):     # loops over parents
            self.s[i] += val       # update node
            i += (i & -i)          # parent

    # variante:
    # pylint: disable=bad-whitespace
    def intervalAdd(self, a, b, val):
        """Variant, adds val to t[a], to t[a + 1] ... and to t[b]

        :param int a b: with 0 <= a <= b < len(t)
        """
        self.add(a,     +val)
        self.add(b + 1, -val)

    def get(self, a):
        """Variant, reads t[a]

        :param int i: negative a will return 0
        """
        return self.prefixSum(a)
# snip}
