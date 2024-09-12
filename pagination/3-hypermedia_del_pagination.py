#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """ Server class, pagnation of a database
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached Dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Index dataset by sorting position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Return a dictionary"""
        indexed_dataset = self.indexed_dataset()

        assert isinstance(index, int) and 0 <= index < len(indexed_dataset), "Invalid Index"

        indexed_keys = list(indexed_dataset.keys())

        data = []
        current_index = index
        while len(data) < page_size and current_index < len(indexed_keys):
            data.append(indexed_dataset[indexed_keys[current_index]])
            current_index += 1

        next_index = current_index if current_index < len(indexed_keys) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
