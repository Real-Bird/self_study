def longestPalindrome(s):
    def expand(left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s
    answer = ""
    for i in range(len(s)-1):
        answer = max(answer, expand(i, i+1,s), expand(i, i+2,s),key=len)
    return answer

print(longestPalindrome("bb"))
print(longestPalindrome("aacabdkacaa"))