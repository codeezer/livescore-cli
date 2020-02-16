#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    module: containing all the backend processes
"""


def find_longest_no(array):
    longest_length = 5
    for data in array:
        n = len(data)
        if n > longest_length:
            longest_length = n
    return longest_length


def get_longest_list(array):
    list2return = [0]*len(array[0])
    for row in array:
        row_length = len(row)
        if isinstance(row, list) is False:
            if row_length > list2return[0]:
                list2return[0] = row_length
        else:
            for i in range(row_length):
                row_row_length = len(row[i].strip())
                if row_row_length > list2return[i+1]:
                    list2return[i+1] = row_row_length

    return list2return
