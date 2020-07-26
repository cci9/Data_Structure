def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j = j - 1
    return nums

if __name__ == '__main__':
    nums = [0,1,5,4,3,8]
    print(insertion_sort(nums))