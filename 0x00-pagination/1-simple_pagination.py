#!/usr/bin/env python3
"""
Tis Module contains a function named index_range that takes
two integer arguments page and page_size
"""
from typing import Tuple, List
import csv
import math


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        returns the appropriate page of the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        indexes = index_range(page, page_size)
        dataset = self.dataset()
        try:
            return dataset[indexes[0]:indexes[1]]
        except IndexError:
            return []
