# def isPalindrome(s: str) -> bool:
#     s = list(s.lower())
#     tmp = ""
#     tmp2 = ""
#     for i in s:
#         if i.isalnum():
#             tmp += i
#             tmp2 = i + tmp2
#     if tmp == tmp2:
#         return True
#     else:
#         return False

# import collections
#
#
# def isPalindrome(s: str) -> bool:
#     strs: Deque = collections.deque()
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
#     return True

import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

print(isPalindrome(s="A man, a plan, a canal: Panama"))
