def longest_run1(s, c):
    run = 0
    max_run = 0

    if c == "z":
        s += "y"
    else:
        s += "z"

    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else:
            run += 1

    return max_run

# Runtime: const1 + len(s) * const2
#          O(n), n = len(s)

# Example 2
def longest_run2(s, ch):
    # at most len(s) times
    for longest in range(len(s), -1, -1):
        cur_run = 0
        # The loop below takes at most len(s)*const operations
        # runs at most len(s) times
        for i in range(len(s)):
            if s[i] == ch:
                # Takes at most const operations
                cur_run += 1
            else:
                cur_run = 0

            if cur_run == longest:
                return longest
    return 0

# In total: at most len(s)*len(s)*const operations
# O(n^2), where n = len(s)

# Example 3:
def f1(x):
    return 2*x

def f2(x):
    return 10*x

def applyit(f, x):
    return f(x)

applyit(f1,5)