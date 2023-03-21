# https://leetcode.com/problems/squares-of-a-sorted-array
from typing import List

class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     # square O(N)
    #     squared = [num*num for num in nums]
    #     # sort (NlogN)
    #     squared.sort()
    #     return squared

    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [None] * len(nums)
        current = len(nums) - 1

        while (current >= 0):
            if abs(nums[left]) < abs(nums[right]):
                result[current] = nums[right] ** 2
                right -= 1
            else:
                result[current] = nums[left] ** 2
                left += 1
            current -= 1
        
        return result

nums = [-4,-1,0,3,10]
sol = Solution()
print(sol.sortedSquares(nums))
