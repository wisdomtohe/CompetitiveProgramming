#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""\
Subsetsum by splitting
christoph dürr et jill-jênn vie - 2014-2018
"""

# snip{
def part_sum(x_table, i=0):
    """All subsetsums from x_table[i:]

    :param x_table: table of values
    :param int i: index_table defining suffix_table of x_table to be considered
    :iterates: over all values, in arbitrary order
    :complexity: :math:`O(2^{len(x_table)-i})`
    """
    if i == len(x_table):
        yield 0
    else:
        for s_idx in part_sum(x_table, i + 1):
            yield s_idx
            yield s_idx + x_table[i]


def subset_sum(x_table, r_target):
    """Subsetsum by splitting

    :param x_table: table of values
    :param r_target: target value
    :returns bool: if there is a subsequence of x_table with total sum r_target
    :complexity: :math:`O(n^{\\lceil n/2 \\rceil})`
    """
    k = len(x_table) // 2              # divide input
    y_value = [v for v in part_sum(x_table[:k])]
    z_value = [r_target - v for v in part_sum(x_table[k:])]
    y_value.sort()                     # test of intersection between y_value and z_value
    z_value.sort()
    i = 0
    j = 0
    while i < len(y_value) and j < len(z_value):
        if y_value[i] == z_value[j]:
            return True
        if y_value[i] < z_value[j]:  # increment index_table of smallest element
            i += 1
        else:
            j += 1
    return False
# snip}
