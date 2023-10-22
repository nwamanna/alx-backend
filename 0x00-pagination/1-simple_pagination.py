#!/usr/bin/env python3
""" a method named get_page that takes two integer arguments
    page with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ a function named index_range that takes two integer arguments
        page and page_size and return a tuple of size two containing
        a start index and an end index corresponding to the range
        of indexes to return in a list for those particular pagination
        parameters
    """
    if page <= 0:
        return (0, page_size)

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return (start_idx, end_idx)


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
        """return page items based on page and page_size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        result = index_range(page, page_size)
        start_idx, end_idx = result

        list_val = self.dataset()

        if start_idx >= len(list_val) or end_idx > len(list_val):
            return []

        return list_val[start_idx:end_idx]
