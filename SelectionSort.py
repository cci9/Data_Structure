def selection_sort(nums):
    for i in range(len(nums) - 1):
        index = i

        for j in range(i + 1, len(nums), 1):
            if nums[j] < nums[index]:
                index = j

        if index != i:
            nums[index], nums[i] = nums[i], nums[index]

    return nums

if __name__ == '__main__':
    nums = [0, -1, -2, -3]
    print(selection_sort(nums))