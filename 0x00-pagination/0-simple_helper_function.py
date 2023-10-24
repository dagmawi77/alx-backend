#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
