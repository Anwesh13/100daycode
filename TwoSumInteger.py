from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Method
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        # HashMap Method
        HashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[n] = i

