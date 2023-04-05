# https://leetcode.com/problems/move-zeroes/

# from typing import List

class Solution:
    """
    """
    # def moveZeroes(self, nums) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     for i in nums:
    #         if i == 0 :
    #             nums.remove(0)
    #             nums.append(0)
    #     return

    # def moveZeroes(self, nums) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     nums.sort(key = lambda x: x == 0)

    def moveZeroes(self, nums) -> None:
        zero_ptr = 0
        number_ptr = 0

        while(number_ptr  < len(nums)):
            if (nums[number_ptr] != 0):
                nums[zero_ptr], nums[number_ptr] = nums[number_ptr], nums[zero_ptr]
                zero_ptr += 1
                
            number_ptr += 1
        
        return


nums = [0,12,0,3,1] #  output [12,3,1,0,0]
# nums = [0]

sol = Solution()
sol.moveZeroes(nums)
print(nums)