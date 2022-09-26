#!/usr/bin/python3
"""Contains the functions to find a peak in a list of
unsorted integers."""


def find_peak(list_of_integers):
    """Returns the peak in a given list."""
    if len(list_of_integers) == 0 or type(list_of_integers) is not list:
        return None
    return search(list_of_integers, 0, len(list_of_integers) - 1)

def search(nums, l, r):
    """Searches nums array recursively using binary search to get
    the peak."""
    if l == r:
        return nums[l]
    mid = int((l + r) / 2)
    if nums[mid] > nums[mid + 1]:
        return search(nums, l, mid)
    return search(nums, mid + 1, r)
