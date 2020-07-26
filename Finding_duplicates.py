def duplicates(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = - nums[abs(num)]
            print(nums)

        else:
            print('Repetition found: ', abs(num))

nums = [2,2,2,1,3,4,5,1,7,6,7,4,3]
duplicates(nums)