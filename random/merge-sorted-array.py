# https://leetcode.com/problems/merge-sorted-array
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = n + m - 1
        n -= 1
        m -= 1
        while(n >= 0 and m >= 0):
            if nums1[m] > nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
            else:
                nums1[pos] = nums2[n]
                n -= 1
            pos -= 1

        if n >= 0:
            nums1[:n] = nums2[:n]

sol = Solution()


def test_4():
    nums1 = [1,2,3,0,0,0,0]
    nums2 = [0,2,5,6]
    m = 3
    n = 4
    sol.merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(nums1)

test_4()