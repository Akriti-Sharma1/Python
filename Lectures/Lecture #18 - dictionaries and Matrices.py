# grades = {"PHY": "A+", "CIV": "A", "CSC": "A+", "ESC": "B+"}
#
# del grades["PHY"]
#
# grades.clear()

def correct_transcript_bad(grades):
    for course in grades:
        if grades[course] not in ["A", "A+"]:
            del grades[course]

def correct_transcript_fixed(grades):
    for course in list(grades.keys()): # for course in ["PHY", "CIV", ...]
        if grades[course] not in ["A", "A+"]:
            del grades[course]

def drop_everything1(grades):
    grades = {} # no effect outside the function

def drop_everything2(grades):
    grades.clear() # does have an effect outside the function

def make_csc_100(grades):
    grades["CSC"] = 100 # has an effect outside the function

def drop_everything3(grades):
    while len(grades) > 0:
        del grades[list(grades.keys()[0])]

# Matrices
def mult_mac_vec(M, Mdim, v):
    '''Multiply the sparse matrix M of dimension Mdim by the vector v'''
    res = 0 * Mdim[0]
    for coords, entry in M.items():
        res[coords[0]] += entry * v[coords[1]]

    return res

if __name__ == "__main__":
    grades = {"PHY": "A+", "CIV": "A", "CSC": "A+", "ESC": "B+"}
    correct_transcript_fixed(grades)
    M = {(0,3): 1, (0,1): 1, (1,4): 5, (2,0): 2}
    Mdim=(3,5)
    v = [1,2,3,4,5]