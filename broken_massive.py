# ID удачной посылки: 75909369
def broken_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        center = nums[mid]
        num_left = nums[left]
        num_right = nums[right]
        if center == target:
            return mid
        elif num_left == target:
            return left
        elif num_right == target:
            return right
        if num_left <= center:
            if num_left < target < center:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if center < target < num_right:
                left = mid + 1
            else:
                right = mid - 1
    return -1
