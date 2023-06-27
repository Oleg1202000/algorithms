# https://leetcode.com/problems/remove-element/submissions/981153793/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeElement(nums: List[int], val: int) -> int:

        k = 0
        for _ in range(len(nums)):
            if nums[k] == val:
                nums.pop(k)
            else:
                k += 1

        return k


nums = list(map(int, input().split(",")))
val = int(input())

print(Solution.removeElement(nums=nums, val=val))
