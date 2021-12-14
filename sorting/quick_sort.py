from random import randint
from typing import List, Tuple


def quick_sort(array: List[int]) -> None:
    """
    Complexity: O(n log n)
    :param array: List of integers to sort
    :return: List of sorted integers
    """
    _quick_sort(array, 0, len(array) - 1)


def _partition(array: List[int], low: int, high: int) -> Tuple[int, int]:
    """
    :param array: Array to sort
    :param low: low index where to start sort in array
    :param high: high index where to end sort in array
    :return: final indexes where sort stops
    """
    pivot = array[low + high // 2]
    i, j = low, high

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    return i, j


def _quick_sort(array: List[int], low: int, high: int) -> None:
    if low < high:
        i, j = _partition(array, low, high)
        _quick_sort(array, low, j)
        _quick_sort(array, i, high)


if __name__ == '__main__':
    unsorted_array = [randint(1, 1000) for _ in range(10)]
    print(f'Before: {unsorted_array}')
    quick_sort(unsorted_array)
    print(f'After: {unsorted_array}')
    assert sorted(unsorted_array) == unsorted_array
