def getCount(loc, num):
    cnt = 0

    if loc % 3 == 1:
        cnt += 1
        loc += 1

    elif loc % 3 == 0:
        cnt += 1
        loc -= 1

    cnt += int(abs(num-loc)/3)
    return cnt


def solution(numbers, hand):
    leftHand = 10
    rightHand = 12
    answer = ''

    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            leftHand = i
        elif i in [3, 6, 9]:
            answer += "R"
            rightHand = i
        else:
            if i == 0:
                i = 11
            left_dist = getCount(leftHand, i)
            right_dist = getCount(rightHand, i)
            if (left_dist > right_dist):
                answer += "R"
                rightHand = i
            elif (left_dist < right_dist):
                answer += "L"
                leftHand = i
            elif (left_dist == right_dist):
                if (hand == "left"):
                    answer += "L"
                    leftHand = i
                elif (hand == "right"):
                    answer += "R"
                    rightHand = i
    return answer
