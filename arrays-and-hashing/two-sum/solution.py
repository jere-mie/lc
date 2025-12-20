# LeetCode: https://leetcode.com/problems/two-sum/
# NeetCode: https://neetcode.io/problems/two-integer-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = dict()
        for i, num in enumerate(nums):
            if target-num in found:
                return [found[target-num], i]
            found[num] = i
