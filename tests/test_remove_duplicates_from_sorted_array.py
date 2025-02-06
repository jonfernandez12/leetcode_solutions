import pytest

from utils.remove_duplicates_from_sorted_array import (
    remove_duplicates_from_sorted,
)


@pytest.mark.parametrize(
    ('nums, result'),
    [([1, 1, 2], [1, 2]), ([[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]])],
)
def test_remove_duplicates_from_sorted(nums: list[int], result: list[int]):
    k = remove_duplicates_from_sorted(nums)

    assert k == len(result)

    for i in range(k - 1):
        assert nums[i] == result[i]
