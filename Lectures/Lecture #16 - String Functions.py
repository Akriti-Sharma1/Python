# "praxis forever" "a prefix rovers"
# ignore spaces --> s1.replace(' ', '')
# ignore cases difference ("Pr" is an anagram of "rp")
def is_anagram(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", "")) # returns a list

num = 180
course_name = "ESC" + str(num)

# Ways to print
"ESC %d %s" % (num, "!") # %d: decimal, #f: float, %s: string
"ESC {}".format(num)
f"ESC{num}"
exec("x = 2")

exec("def f():\n return 42")


# generate all strings of length n over an alphabet

'''
for letter0 in alphabet:
    for letter1 in alphabet:
    ....
    '''

def gen_nested_loop(n):
    ''' Generated python code to print all strings of length n over the alphabet (a list) '''

    res = "def gen_password(): \n"
    for i in range(n):
        res += " " * (i + 1) + f"for letter{i} in alphabet:\n"

    res += " " * (n + 1)
    res += "print("
    for i in range(n-1):
        res += f"letter{i} + "
    res += f"letter{n-1}"
    res += ")"

    return res

# code = gen_nested_loop(10)
# alphabet = "abcd"
# exec(code)
# gen_password()

# given a string s, want to determine the longest run of character c in s
# >>> longest_run("abbbbcbbc", "b")
# 4

#>>>> longest_run("abbbcbbc", "c")
# 1

def longest_run(s,c):
    count = 0
    longest = 0
    for i in s:
        if i == c:
            count += 1
        else:
            if count > longest:
                longest = count
            else:
                longest = longest
            count = 0

    return longest

def longest_run_real(s, c):
    for run in range(len(s), 0, -1):
        if run * c in s:
            return run
        return 0

def longest_run_real_2(s,c):
    max_run = 0 # the largest run we saw thus far
    run = 0 # the length of the current run
    '''
    if c == "z":
        s = s + "y"
    else:
        s = s + "z"
    '''

    for ch in s:
        if ch != c:
            max_run = max(max_run, run)
        else:
            run += 1

    return max(max_run, run)


# s = "xaaxaaabcaaaabbx"

def n_as_plus_b(s,n):
    '''Return True is s contains exactly n "a"s followed by exactly one "b"
    '''
    # can't say "a"*n+"b" in s
    # Idea: Keep track of the current run of "a"s, if we see a "b", check that it's not followed by a "b"
    cur_run_a = 0
    for i in range(len(s)):
        if s[i] == "a":
            cur_run_a += 1
        elif s[i] == "b":
            if cur_run_a == n:
                if s[i+1] != "b":
                    return True
                elif i == len(s) - 1: # We are at the end of s
                    return True
        else:
            cur_run_a = 0

    return False

if __name__ == "__main__":
    print(longest_run("abbbcbbc", "c"))
    s = "xaaxaaabcaaaabbx"
    print(n_as_plus_b(s,4))








