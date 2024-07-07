"""
    This module contains the following sorting algorithms:
    - Insertion sort
    - - Involves splitting the array into two parts: sorted and unsorted. The sorted part is empty at the beginning and the unsorted part contains all the elements. The algorithm then iterates over the unsorted part, removing one element at a time and inserting it into the correct position in the sorted part. Very simple to implement and efficient for small arrays.
    - - Time complexity: O(n^2) in the worst case, O(n) in the best case, and O(n^2) in the average case.
    - - Space complexity: O(1).
"""

def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    :param arr: The array to be sorted.
    :return: The sorted array.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    :param arr: The array to be sorted.
    :return: The sorted array.
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j + 1 < len(arr) and arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
# print(insertion_sort(arr))
# print(bubble_sort(arr))
