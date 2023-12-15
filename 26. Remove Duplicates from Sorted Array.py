from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[counter] = nums[i]
                counter += 1
        return counter


result = Solution()

print(result.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

print(result.removeDuplicates([1, 1, 2]))
