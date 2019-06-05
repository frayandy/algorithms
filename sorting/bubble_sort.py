from random import randint
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """
    Complexity - O(n2)
    :param array: List of integers to sort
    :return: List of sorted integers
    """
    array_len = len(array)
    for i in range(array_len):
        for e in range(array_len):
            if array[e] > array[i]:
                array[i], array[e] = array[e], array[i]
    return array


if __name__ == '__main__':
    unsorted_array = [randint(1, 1000) for _ in range(10)]
    print(f'Before: {unsorted_array}')
    print(f'After: {bubble_sort(unsorted_array)}')
