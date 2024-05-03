#!/usr/bin/env python3
"""This module defines index_range and class Server"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """Returns tuple containing the beginning and end of pages base on index"""

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This method takes two args to retiv a index value"""

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        data = self.dataset()
        if page_size > len(data):
            return []
        desired_pages = index_range(page, page_size)
        return data[desired_pages[0]:desired_pages[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """This method returns a dictionary with data from dataset"""

        #code goes here