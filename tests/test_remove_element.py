import pytest

from utils.remove_element import remove_elements


@pytest.mark.parametrize(
    ('nums, val, result'),
    [([3, 2, 2, 3], 2, [3, 3]), ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 0, 1, 3, 4])],
)
def test_remove_elements(nums, val, result):
    k = remove_elements(nums, val)
    assert k == len(result)

    nums[:k] = sorted(nums[:k])
    i = 0
    for i in range(k):
        assert nums[i] == result[i]
