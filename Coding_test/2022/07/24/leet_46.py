# from itertools import permutations
#
# def permute(nums):
#     answer = []
#     for i in permutations(nums):
#         answer.append(list(i))
#     return answer
#
# print(permute([0, 1]))

def permute(nums: list):
    answer = []
    prev_elements = []

    def dfs(elements: list):
        if len(elements) == 0:
            answer.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return answer


print(permute([0, 1]))