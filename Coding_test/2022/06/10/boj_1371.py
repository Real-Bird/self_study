from sys import stdin

string, word = stdin.read(), [0 for i in range(26)]
for s in string:
    if s.islower():
        word[ord(s)-97] += 1
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end='')