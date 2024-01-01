#!/usr/bin/env python3
"""
a function named index_range that takes two integer arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    if page <= 0 and page_size <= 0:
        return None
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
