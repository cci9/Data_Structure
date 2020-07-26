def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - 1 - i, 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
    return nums
def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

if __name__ == '__main__':
    a = [1,2,8,4,6,3,0,8,-5,1]
    print(bubble_sort(a))