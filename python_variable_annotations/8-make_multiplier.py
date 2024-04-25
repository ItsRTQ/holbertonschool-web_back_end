#!/usr/bin/env python3
"""This module define make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """this method reutnrs a function a multiples values"""

    def func(num: float) -> float:
        """This method multimples numbers by mutiplier"""

        return num * multiplier
    return func
