import time

TIMER_NUM = 100000

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()

        for i in range(TIMER_NUM):
            func(*args, **kwargs)

        end = time.time()

        result = end - start

        print(f"time wasted: {result}")

    return inner


@timer
def moveZeroes(nums) -> None:
        zero_ptr = 0
        number_ptr = 0

        while(number_ptr  < len(nums)):
            if (nums[number_ptr] != 0):
                nums[zero_ptr], nums[number_ptr] = nums[number_ptr], nums[zero_ptr]
                zero_ptr += 1
                
            number_ptr += 1
        
        return

@timer
def moveZeroes2(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:
        if i == 0 :
            nums.remove(0)
            nums.append(0)
    return


# nums = [1,0,4,5,0,10]
# moveZeroes(nums)
# moveZeroes2(nums)


@timer
def twoSum(numbers, target):
        first = 0
        second = len(numbers) - 1

        while (first < second):
            current = numbers[first] + numbers[second]
            if (current > target):
                second -= 1
                continue
            if (current < target):
                first += 1
                continue
            return [first+1, second+1]

@timer
def twoSum2(numbers, target):
    nums = {}
    for idx, num in enumerate(numbers):
        need = target - num
        if (need in nums.keys()):
            return [nums[need] + 1, idx + 1]
        else:
            nums[num] = idx


numbers = [2,7,11,15]
target = 9

twoSum(numbers, target)
twoSum2(numbers, target)