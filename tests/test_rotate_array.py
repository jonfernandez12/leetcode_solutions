import pytest

from utils.rotate_array import rotate


@pytest.mark.parametrize(
    'nums, k, result',
    [
        ([1, 2, 3, 4, 5, 6, 7], 2, [6, 7, 1, 2, 3, 4, 5]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_rotate(nums, k, result):
    rotate(nums, k)
    assert nums == result
