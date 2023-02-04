
def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    indexes = []
    for i in range(len(s)):
        if s[i] == " ":
            indexes.append(i)
    try:
        index = max(indexes)
        length = len(s) - index - 1
        return length
    except:
        return len(s)


""" 
# so smart 
s = s.split()
return len(s[-1])
    
"""



s = " "

print(lengthOfLastWord(s))
