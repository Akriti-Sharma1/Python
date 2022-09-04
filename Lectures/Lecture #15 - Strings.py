# Strings

s1 = "praxis"
s2 = "esc180"

s1 = "P" + s1[1:]
print(s1)

s2 = s2[:2] + "C" + s2[3:] # len(s2) = 6
print(s2)

s1.upper()
print(s1)

# Reverse a string

s1 = "praxis"
s1[::-1]

def reverse_str(s):
    res = ""
    for i in range(len(s)-1,-1,-1):
        res += s[i] # res = res + s[i]
    return res

def reverse_str2(s):
    res = ""
    for i in range(len(s)):
        res = s[i] + res
    return res

def reverse_str3(s):
    res = ""
    for c in s:
        res = c + res
    return res

for c in s1:
    print(c)

# Anagram of s is a string that contains all the same characters as s
#"praxis forever" and "a prefix rovers" are anagrams

def is_anagram(s1, s2):
    ''' Return True iff s1 and s2 are anagrams, not counting spaces
        (repition of characters is fine)
    '''
    for c in s1:
        if c == " ":
            continue
        if s1.count(c) != s2.count(c):
            return False

    for c in s2:
        if c == " ":
            continue
        if s1.count(c) != s2.count(c):
            return False

    return True

def is_anagram2(s1, s2):
    ''' Return True iff s1 and s2 are anagrams, not counting spaces
        (repition of characters is fine)
    '''
    for c in s1 + s2:
        if c == " ":
            continue
        if s1.count(c) != s2.count(c):
            return False

    return True



















