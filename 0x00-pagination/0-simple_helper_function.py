#!/usr/bin/env python3
"""
Tis Module contains a function named index_range that takes
two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination
    parameters
    """
    if page <= 0 and page_size <= 0:
        return None
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
