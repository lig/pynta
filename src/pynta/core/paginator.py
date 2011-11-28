"""
We could use django.core.paginator probably, but it is not necessary for now.
Also let's try to implement something more pythonish.
"""

from collections import Sequence, Iterable
from math import ceil


class Paginator(Sequence):

    def __init__(self, dataset, page_size=None):

        if isinstance(dataset, Iterable):
            self.data = dataset
        else:
            raise TypeError('dataset must be an instance of any iterable')

        self.page_size = page_size or 0


    def get_page(self, page_num):
        return self[int(page_num) - 1]


    def __getitem__(self, index):
        page_start = index * self.page_size
        page_end = min(page_start + self.page_size, len(self.data))
        dataslice = self.data[page_start:page_end]
        return Page(dataslice, index, len(self), self)


    def __len__(self):
        return (self.page_size and
            ceil(float(len(self.data)) / self.page_size) or 1)


class Page(Sequence):

    def __init__(self, dataslice, page_num, num_pages, paginator):

        if isinstance(dataslice, Iterable):
            self.data = dataslice
        else:
            raise TypeError('dataslice must be an instance of any iterable')

        self.page_num = page_num
        self.num_pages = num_pages
        self.paginator = paginator


    def __getitem__(self, index):
        return self.data[index]


    def __len__(self):
        return len(self.data)
