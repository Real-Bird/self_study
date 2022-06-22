import re
from collections import Counter


def mostCommonWord(paragraph, banned):
    p = re.sub("[^\w]", " ", paragraph.lower())
    string = [word for word in p.split() if word not in banned]
    c = Counter(string).most_common(1)
    return c[0][0]


print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c", banned=["a"]))