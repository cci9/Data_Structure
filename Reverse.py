def reverse(nums):
    startIndex = 0
    endIndex = len(nums) - 1
    while endIndex > startIndex:
        nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]
        startIndex = startIndex + 1
        endIndex = endIndex - 1
    return nums
if __name__ == '__main__':

    nums = [1,2,3,4,5]
    print(reverse(nums))



