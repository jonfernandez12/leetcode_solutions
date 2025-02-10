from collections import Counter

"""

Code
Testcase
Test Result
Test Result
169. Majority Element
Solved
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""


def majority_element(nums: list[int]) -> int:
    threshold = len(nums) / 2
    count = Counter(nums)
    count = dict(count)
    return next(i[0] for i in count.items() if i[1] > threshold)


def majority_element_wtih_hashmap(nums: list[int]) -> int:
    hash = {}
    majority_element, majority_count = 0, 0
    for i in nums:
        hash[i] = 1 + hash.get(i, 0)
        if hash[i] > majority_count:
            majority_element = i
            majority_count = hash[i]
    return majority_element
