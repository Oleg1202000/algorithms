# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeDuplicates(nums: List[int]) -> int:

        k = 0
        second_index = 1
        while second_index != len(nums):
            if nums[k] < nums[second_index]:
                nums[k+1], nums[second_index] = nums[second_index], nums[k+1]
                k += 1
            else:
                second_index += 1

        print(nums)

        return k + 1


nums = list(map(int, input().split(",")))

print(Solution.removeDuplicates(nums=nums))
