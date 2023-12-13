from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        return counter


result = Solution()

print(result.removeElement([3, 2, 2, 3, 3, 2, 5, 6, 2, 5, 4], 3))
print(result.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
