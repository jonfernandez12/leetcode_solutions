"""
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element
appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in
some languages, you must instead have the result be placed in
 the first part of the array nums. More formally, if there are k
 elements after removing the duplicates, then the first k elements
 of nums should hold the final result. It does not matter what you
 leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by
modifying the input array in-place with O(1) extra memory.

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


def remove_double_duplicates_from_sorted(nums: list[int]) -> int:
    """
    Time complexity: O(nums)
    Space complexity: O(1)
    """
    index = 2
    for i in range(2, len(nums)):
        if nums[index - 2] != nums[i]:
            nums[index] = nums[i]
            index += 1
    return index
