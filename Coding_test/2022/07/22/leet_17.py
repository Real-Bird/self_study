def letterCombinations(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in dial[digits[i]]:
                dfs(i + 1, path + j)
    if not digits:
        return []
    dial = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    result = []
    dfs(0, "")

    return result

print(letterCombinations("23"))