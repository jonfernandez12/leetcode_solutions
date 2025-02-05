import pytest
from utils.merge_sorted_arrays import merge_sorted_arrays

@pytest.mark.parametrize(('nums1, nums2, result'), [
        ([1,2,5,0,0,0], [8,9,10], [1,2,5,8,9,10]),
        ([4,5,6,0,0,0], [1,2,3], [1,2,3,4,5,6]),
        ([7,8,9,0,0,0], [2,5,6], [2,5,6,7,8,9]),])
def test_merged_sorted_arrays(nums1, nums2, result):
    merge_sorted_arrays(nums1, 3, nums2, 3)
    assert nums1 == result