# Tuples
# Like lists, but immutable

t = (2,3,4)
t[0]
t[1:]

#t[0] = 5 # Will give you an error

t = ([1,2],3)
t[0][0] # allowed
#t[0] = 6 # Not allowed

t = ("a", "b", "c")
x,y,z = t
#x,y = t # Not allowed

x, y = y, x

def f():
    return 42, 43

x = f() # x is the touple (42,43)
y, z = f() # y is 42, z is 43

# Dictionaries
# a set of key, value pairs
# keys are unique, values can repeat

grades = {"PHY": 90, "MAT": 80, "CSC": 90}
grades["MAT"]

kids = ["Bob", "Dorothy", "Alice"]
faves = ["candy", "costumes", "midterms"]
# kids[i] corresponds to faves[i]
faves_dict = {"Bob": "candy", "Dorothy": "costumes", "Alice": "midterms"}

grades["CIV"] = 95

# Data on the UofT endowment
endowment = {2012: 1518, 2014: 1881, 2015: 2142, 2021: 3150} # immutable

#endowment[[1,2]] = 5 # Not allowed
endowment[(1,2)] = 5 # Appends touple to the end of the list

grades = {"PHY": 90, "MAT": 80, "CSC": 90}
grades["CIV"] = 95
list(grades.keys())
list(grades.values())

for subj in grades:
    print(subj) # not always in the order in the dictionary
    print(f"I got {grades[subj]} in {subj}")

grades.items() # returns all the items as touples

for subj, grade in grades.items():
    print(f"I got {grade} in {subj}")

grades = {"PHY": 90, "MAT": 80, "CSC": 90}
grades["CIV"] = 95

def get_subj_by_grade(grades, grade):
    res = []
    for subj, gr in grades.items():
        if gr == grade:
            res.append(subj)
    return res

# want to invert the dictionary grades:
# keys will be the grades, values will be the subjects
{90: ["PHY", "CSC"], 80: ["MAT"], 95: ["CIV"]}

def get_inv_grades(grades):
    res = {}
    for subj, grade in grades.items():
        if grade in res:  # same as grade in res.keys()
            res[grade].append(subj)
        else:
            res[grade] = [subj]

L = [3,4,2,1,2]

# for i in range(len(L)): # dame as for i in range(5), doesn't update when the list gets shorter, gives error
#     if L[i] == 4.0:
#         del L[i]

i = 0
while i < len(L):
    if L[i] == 4.0:
        L[i]
    i += 1

L = [3,4,2,1,2]
i = 0
while i < len(L):
    if L[i] == 4.0:
        del L[i]
    i += 1

L = [3,4,4,2,1,2]
i = 0
while i < len(L):
    if L[i] == 4.0:
        del L[i]
    else:
        i += 1

L = [3,4,4,2,1,2]
L_new = []
for e in L:
    if e != 4.0:
        L_new.append(e)
