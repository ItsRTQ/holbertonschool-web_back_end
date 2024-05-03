#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a paginated subset of the dataset with pagination info.
        Args:
            index (int): Start index of the page, default: 0.
            page_size (int): Size of each page, default: 1).
        Returns:
            Dict[str, Union[int, List]]: Pagination information and data.
        """

        assert index >= 0, "Invalid index"
        assert page_size > 0, "Invalid page size"
        dataset = self.dataset()
        total_items = len(dataset)
        start_index = index
        end_index = min(index + page_size, total_items)
        data = dataset[start_index:end_index]
        next_index = end_index if end_index < total_items else None
        pagination_info = {
            'index': start_index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
        return pagination_info
