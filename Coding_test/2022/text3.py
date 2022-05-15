def inspect_str(s,n):
    x = map(''.join, zip(*[iter(s)] * n))
    temp = []
    for i in x:
        temp.append(i)
    print(temp)
    return temp

def solution(replies, n, k):
    answer = []
    for reply in replies:
        cnt = 1
        i = 0
        for length in range(n, len(reply)//2+1):
            arr = inspect_str(reply[i:], length)
            x = ""
            for insp in arr:
                if x == insp:
                    cnt += 1
                else:
                    break
                x = insp
            if cnt >= k:
                break
            else:
                cnt = 1
            i += 1
        if cnt > 1:
            answer.append(0)
        else:
            answer.append(1)
    return answer

print(solution(["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"],3,2))
print(solution(["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"], 2, 4))