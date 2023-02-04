def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:  # check if char c was used and if this char is in sequence right now
            start = used[c] + 1  # if it is, meaning it's end of valid substring => set start value to previous occurence of this letter + 1
        else:
            max_length = max(max_length, i - start + 1)  # else check if current "streak" is greater than max_length

        used[c] = i  # add char with its index to dict

    return max_length


s = "pwwkew"
print(lengthOfLongestSubstring(s))

