# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    # def twoSum(self, numbers, target):
    #     first = 0
    #     second = len(numbers) - 1

    #     while (first < second):
    #         current = numbers[first] + numbers[second]
    #         if (current > target):
    #             second -= 1
    #             continue
    #         if (current < target):
    #             first += 1
    #             continue
    #         return [first+1, second+1]


    def twoSum(self, numbers, target):
        nums = {}
        for idx, num in enumerate(numbers):
            need = target - num
            if (need in nums.keys()):
                return [nums[need] + 1, idx + 1]
            else:
                nums[num] = idx



numbers = [2,7,11,15]
target = 9



sol = Solution()
sol.twoSum(numbers, target)


print()