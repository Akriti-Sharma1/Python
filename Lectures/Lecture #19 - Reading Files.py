f = open("hello.txt", encoding = "latin1")
s = f.read() # returns a string that contains the contents of the file
print(s)

s.split("\n") # gives a list of components list s

"Engineers rules the world".split(" ")

s.split("\n")[2] # gives the 12th line of the file

def num_words(text):
    return len(text.split(" ")) # approximation of # of words in the text\

def num_words_file(filename):
    f = open(filename, encoding = "latin1")
    s = f.read()
    return len(s.split(" "))

def num_sentences(text):
    # assume that sentences are separated by "!"s and "."s and "?"s
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    return len(text.split("."))