#!/usr/bin/env python3
"""This module defines sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This method takes a list with mix values and returns it total"""

    total: float = 0.0
    for i in mxd_lst:
        total += i
    return total
