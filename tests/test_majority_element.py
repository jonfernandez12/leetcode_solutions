from utils.majority_element import majority_element, majority_element_wtih_hashmap
import pytest

@pytest.mark.parametrize('nums, result',[
                          ([3,2,3], 3),
                          ([2,2,1,1,1,2,2], 2),])
def test_majority_element(nums: list[int], result: int):
    assert majority_element(nums) == result

@pytest.mark.parametrize('nums, result',[
                          ([3,2,3], 3),
                          ([2,2,1,1,1,2,2], 2),])
def test_majority_element_wtih_hashmap(nums: list[int], result: int):
    assert majority_element_wtih_hashmap(nums) == result