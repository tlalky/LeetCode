def longestCommonPrefix(strs: list[str]) -> str:
    strs.sort()
    result = ''
    i = 0
    for letter in strs[0]:
        for word in strs:
            if letter != word[i]:
                return result
        result += letter
        i += 1
    return result
