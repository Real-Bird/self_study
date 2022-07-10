def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer

print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))