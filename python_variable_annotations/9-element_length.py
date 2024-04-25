#!/usr/bin/env python3
""" This funciton defines element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This method retrives the length of elements"""

    return [(i, len(i)) for i in lst]
