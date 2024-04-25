#!/usr/bin/env python3
"""This module defines method sum_list"""

def sum_list(input_list: list) -> float:
    """this method takes a list a sums them"""
    total: float = 0.0
    for i in input_list:
        total += i
    return total
