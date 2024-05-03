#!/usr/bin/env python3
"""This module defines index_range to be use else where"""


def index_range(page, page_size):
    """Returns tuple containing the beginning and end of pages base on index"""

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
