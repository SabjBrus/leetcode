class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index = []
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    nums_index.append(x)
                    nums_index.append(y)
                    return nums_index


n = Solution()
print(n.twoSum([2, 7, 8, 4], 9))
print(n.twoSum([2, 7, 8, 4], 6))
