# https://leetcode.com/problems/rotate-array
from typing import List

class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     shift = k % len(nums)
    #     nums[:] = nums[-shift:] + nums[:-shift]

    # def reverse_in_place(self, nums, start, end):
    #     while(start < end):
    #         nums[start], nums[end] = nums[end], nums[start]
    #         start += 1
    #         end -= 1

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     shift = k % len(nums)

    #     self.reverse_in_place(nums, 0, len(nums) - 1)
    #     self.reverse_in_place(nums, 0, shift - 1)
    #     self.reverse_in_place(nums, shift, len(nums) - 1)

    #     return None

    # def rotate(self, nums: List[int], k: int) -> None:
    #     shift = k % len(nums)
    #     for i in range(shift):
    #         num = nums.pop()
    #         nums.insert(0, num)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break 
            
            start += 1
        


nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(nums)