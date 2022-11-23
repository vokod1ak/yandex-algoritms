# ID удачной посылки: 75770439
def broken_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        center = nums[mid]
        if center == target:
            return mid
        if nums[left] <= center:
            if nums[left] == target:
                return left
            elif nums[left] < target < center:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] == target:
                return right
            elif center < target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
