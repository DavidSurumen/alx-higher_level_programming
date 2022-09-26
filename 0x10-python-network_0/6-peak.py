#!/usr/bin/python3
"""Contains the functions to find a peak in a list of
unsorted integers."""


def find_peak(list_of_integers):
    """Returns the peak in a given list."""
    if len(list_of_integers) == 0 or type(list_of_integers) is not list:
        return None
    return search(list_of_integers, 0, len(list_of_integers) - 1)


def search(nums, left_index, right_index):
    """Searches nums array recursively using binary search to get
    the peak."""
    if left_index == right_index:
        return nums[left_index]
    mid = int((left_index + right_index) / 2)
    if nums[mid] > nums[mid + 1]:
        return search(nums, left_index, mid)
    return search(nums, mid + 1, right_index)
