# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        index_1 = m - 1
        index_2 = n - 1

        while True:
            if index_1 < 0:
                nums1[0:index_1+index_2+2] = nums2[0:index_2+1]
                break
            elif index_2 < 0:
                nums1[0:index_1+index_2+2] = nums1[0:index_1+1]
                break

            if nums1[index_1] > nums2[index_2]:
                nums1[index_1+index_2+1] = nums1[index_1]
                index_1 -= 1
            elif nums1[index_1] < nums2[index_2]:
                nums1[index_1+index_2+1] = nums2[index_2]
                index_2 -= 1
            else:
                nums1[index_1+index_2+1] = nums1[index_1]
                nums1[index_1+index_2] = nums2[index_2]
                index_1 -= 1
                index_2 -= 1

        return nums1


nums1 = list(map(int, input().split(",")))
m = int(input())
nums2 = list(map(int, input().split(",")))
n = int(input())
print(Solution.merge(nums1=nums1, m=m, nums2=nums2, n=n))
