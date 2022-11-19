# ID удачной посылки: https://contest.yandex.ru/contest/24735/run-report/75318722/
def broken_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    arr = [0, 2, 6, 7, 8, 9, 10]
    assert broken_search(arr, 9) == 5
