# 704. Binary Search
class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    # def search(self, nums, target):
    #     index = -1
    #     for i, num in enumerate(nums):
    #         if num == target:
    #             index = i
    #             break
    #     return index

    def search(self, nums, target):
        left = 0
        right = len(nums) - 1


        while (right >= left):
            center_idx = left + (right-left) // 2

            if nums[center_idx] == target:
                return center_idx
            elif nums[center_idx] < target:
                left = center_idx + 1
            else: 
                right = center_idx - 1

        return -1


nums = [-1,2,3]
target = 3

a = Solution()
result = a.search(nums, target)
print(result)