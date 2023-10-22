#!/usr/bin/env python3
""" a function named index_range that takes two integer arguments
    page and page_size and return a tuple of size two containing
    a start index and an end index corresponding to the range
    of indexes to return in a list for those particular pagination parameters
"""
from typing import Tuple


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
