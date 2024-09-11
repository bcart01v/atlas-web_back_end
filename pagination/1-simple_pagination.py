#!/usr/bin/env python3
""" Module that contains a simple helper function
"""
import csv
import math
from typing import List


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
            """ Get the page of the dataset.
            """
            assert isinstance(page, int) and page > 0, "page should be a positive integer"
            assert isinstance(page_size, int) and page_size > 0, "page_size should be a positive integer"

            start_index, end_index = self.index_range(page, page_size)

            dataset = self.dataset()

            if start_index >= len(dataset):
                 return []
            return dataset[start_index:end_index]



    def index_range(self, page: int, page_size: int) -> tuple:
        """ Return a tuple of size two containing a start index and an end index
        """

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)
