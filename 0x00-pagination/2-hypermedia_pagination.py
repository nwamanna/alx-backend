#!/usr/bin/env python3
""" a method named get_page that takes two integer arguments
    page with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Tuple, Dict


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
#     page_size: the length of the returned dataset page
#   page: the current page number
#   data: the dataset page (equivalent to return from previous task)
#   : number of the next page, None if no next page
#   prev_page: number of the previous page, None if no previous page
#   total_pages: the total number of pages in the dataset as an integer

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ method that takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs
        """
        length = len(self.dataset())
        hyper_dict = {}
        hyper_dict['page'] = page
        hyper_dict['data'] = self.get_page(page, page_size)
        hyper_dict['prev_page'] = page - 1
        if hyper_dict['data'] == []:
            hyper_dict['page_size'] = 0
            hyper_dict['next_page'] = 'None'
        else:
            hyper_dict['page_size'] = page_size
            hyper_dict['next_page'] = page + 1
        hyper_dict['total_pages'] = math.ceil(length / page_size)

        return hyper_dict
