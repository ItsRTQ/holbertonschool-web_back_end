#!/usr/bin/env python3
"""This module takes defines to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this method return a tuple of k & v"""

    value = v * v
    return (k, float(value))
