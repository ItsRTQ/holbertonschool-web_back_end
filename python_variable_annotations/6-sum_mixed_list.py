#!/usr/bin/env python3
"""This module defines sum_mixed_list"""


def sum_mixed_list(mxd_lst: list) -> float:
    """This method takes a list with mix values and returns it total"""

    total: float = 0.0
    for i in mxd_lst:
        total += i
    return total
