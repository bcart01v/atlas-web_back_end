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
        """ Return a dictionary with deletion-resilient pagination """
        indexed_dataset = self.indexed_dataset()

        # Ensure index is within bounds
        assert isinstance(index, int) and 0 <= index < len(self.__dataset), "Invalid Index"

        indexed_keys = list(indexed_dataset.keys())
        data = []
        current_index = index
        count = 0

        # Collect the data while skipping deleted entries
        while count < page_size and current_index < len(indexed_keys):
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
                count += 1
            current_index += 1

        # Set the next index
        next_index = current_index if current_index < len(indexed_keys) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }