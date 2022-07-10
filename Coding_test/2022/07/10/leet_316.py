from collections import Counter

def removeDuplicateLetters(s):
    cnt, seen, stack = Counter(s), set(), []
    for char in s:
        cnt[char] -= 1
        if char in seen:
            continue
        while stack and char < stack[-1] and cnt[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return "".join(stack)


print(removeDuplicateLetters("bcabc"))