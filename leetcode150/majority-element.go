package leetcode150
func majorityElement(nums []int) int {
    major := nums[0]
    count := 1

    for _, val := range nums {
        if (major != val) {
            count--
        } else {
            count++
        }

        if (count == 0){
            count = 1
            major = val
        }
    }

    return major
}