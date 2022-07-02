def arrayPairSum(nums):
    nums.sort()
    answer = 0
    for i in range(len(nums) // 2):
        answer += min(nums[2 * i], nums[2 * i + 1])
    return answer


print(arrayPairSum([1, 4, 3, 2]))


def arrayPairSum(nums):
    return sum(sorted((nums))[::2])


print(arrayPairSum([1, 4, 3, 2]))