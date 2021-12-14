from itertools import chain
from random import randint
from typing import List


def quick_sort_recursion(array: List[int]) -> List[int]:
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]
    less_than_pivot = [x for x in array if x < pivot]
    equal_to_pivot = [x for x in array if x == pivot]
    greater_than_pivot = [x for x in array if x > pivot]
    return [
        x for x in chain(
            quick_sort_recursion(less_than_pivot),
            equal_to_pivot,
            quick_sort_recursion(greater_than_pivot)
        )
    ]


if __name__ == '__main__':
    unsorted_array = [randint(1, 1000) for _ in range(10)]
    print(f'Before: {unsorted_array}')
    sorted_array = quick_sort_recursion(unsorted_array)
    print(f'After: {sorted_array}')
    assert sorted(unsorted_array) == sorted_array
