from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams["".join(sorted(word))].append(word)
        # anagrams["".join(sorted(word))].sort()
        sorted(anagrams["".join(sorted(word))])
    answer = list(anagrams.values())
    # answer.sort(key=lambda x: len(x))
    sorted(answer, key=lambda x: len(x))
    return answer


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# sort() Runtime : 227ms
# sorted() Runtime : 179ms