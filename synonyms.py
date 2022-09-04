import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    # This function returns the cosine similarity between the sparse vectors vec1 and vec2, stored as dictionaries.
    num = 0
    vec1_keys = [*vec1]
    vec2_keys = [*vec2]
    vec1_norm = norm(vec1)
    vec2_norm = norm(vec2)
    denom = vec1_norm * vec2_norm
    for i in range(len(vec1_keys)):
        #print(vec1_keys[i])
        if vec1_keys[i] in vec2_keys:
            num += vec1[vec1_keys[i]] * vec2[vec1_keys[i]]
            #print(vec1_keys[i])
    cosine = num / denom
    return cosine

# print(cosine_similarity({"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}, {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}))
# print(cosine_similarity({"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}, {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}))
#print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
# print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))

def build_semantic_descriptors(sentences):
# This function takes in a list sentences which contains lists of strings (words) representing sentences, and returns a dictionary d such that for every word w that appears in at least one of the sentences, d[w] is itself a dictionary which represents the semantic descriptor of w (note: the variable names here are arbitrary).
# Do not have O(n^2) complexity
    semantics ={}
    for sentence in sentences:
        new = []
        sentence = [word.lower() for word in sentence]
        for word in sentence:
            word = word.lower()
            if word in new:
                new.append(word)
            elif word not in new:
                if word not in semantics:
                    semantics[word]={}

                checker = []
                for new_word in sentence:
                    if new_word not in checker:
                        if new_word != word:
                            if new_word in semantics[word]:
                                semantics[word][new_word] += 1
                                checker.append(new_word)
                            else:
                                semantics[word][new_word] =1
                            checker.append(new_word)


    return semantics


#print(build_semantic_descriptors([['akriti', 'bad', 'dad'], ['d', 'a', 'a', 'a'], ['t', 'b']]))
# print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
# ["I", "am", "a", "spiteful", "man"],
# ["I", "am", "an", "unattractive", "man"],
# ["I", "believe", "my", "liver", "is", "diseased"],
# ["however", "I", "know", "nothing", "at", "all", "about", "my",
# "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))

def build_semantic_descriptors_from_files(filenames):
# This function takes a list of filenames of strings, which contains the names of files (the first one can be opened using open(filenames[0], "r", encoding="latin1")), and returns the a dictionary of the semantic descriptors of all the words in the files filenames, with the files treated as a single text. You should assume that the following punctuation always separates sentences: ".", "!", "?", and that is the only punctuation that separates sentences. You should also assume that that is the only punctuation that separates sentences. Assume that only the following punctuation is present in the texts: [",", "-", "--", ":", ";"].
    new = []
    semantics_real = {}
    for name in filenames:
        file = open(name, "r", encoding = "utf-8-sig")
        file = file.read()
        file = file.lower()
        #print(file)
        file = file.replace("\n", " ")
        file = file.replace(","," ")
        file = file.replace("("," ")
        file = file.replace(")"," ")
        file = file.replace("-"," ")
        file = file.replace("--"," ")
        file = file.replace(':', " ")
        file = file.replace(';', " ")
        file = file.replace('"', " ")
        file = file.replace("]", " ")
        file = file.replace("'", " ")

        file = file.replace("? ",".")
        file = file.replace("! ",".")
        file = file.replace(". ",".")

        file = file.split(".")
        for c in file:
            #print(c.split(" "))
            new.append(c.split(" "))
    #print(new)
            #for i in c:
             #   print("1",i)
        #file = file.split(" ")
        #print(file)
    for j in new:
        if j == []:
            new.remove(j)
        for k in j:
            if k == '':
                j.remove(k)
    semantics = build_semantic_descriptors(new)
    #print(new)
    for i in semantics:
        if i in semantics_real:
            for j in semantics[i]:
                if j not in semantics_real[i]:
                    semantics_real[i][j] = semantics[i][j]
                else:
                    semantics_real[i][j] += semantics[i][j]
        else:
            if '' == semantics[i]:
                continue
            semantics_real[i] = semantics[i]

    return semantics_real

#filenames = ["warandpeace.txt", "swannsway.txt"]
#print(build_semantic_descriptors_from_files(filenames))

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
#This function takes in a string word, a list of strings choices, and a dictionary semantic_descriptors which is built according to the requirements for build_semantic_descriptors, and returns the element of choices which has the largest semantic similarity to word, with the semantic similarity computed using the data in semantic_descriptors and the similarity function similarity_fn. The similarity function is a function which takes in two sparse vectors stored as dictionaries and returns a float. An example of such a function is cosine_similarity. If the semantic similarity between two words cannot be computed, it is considered to be −1. In case of a tie between several elements in choices, the one with the smallest index in choices should be returned (e.g., if there is a tie between choices[5] and choices[7], choices[5] is returned).
    index = 0
    checker = 0
    check = True
    if word not in semantic_descriptors:
        similarity = -1
        index = 0
        check = False
    for choice in choices:
        if choice not in semantic_descriptors:
            similarity = -1
            index = 0
            check = False
    if check == True:
        for choice in range(len(choices)):
            #print(choice, choices[choice])
            #print(semantic_descriptors[choices[choice]], semantic_descriptors[word])
            if choices[choice] not in semantic_descriptors:
                pass
            else:
                similarity = similarity_fn(semantic_descriptors[choices[choice]], semantic_descriptors[word])
                if similarity > checker:
                    checker = similarity
                    index = choice
                #print(choices[choice],checker)
    return choices[index]


list = [['a', 'b', 'd'], ['d', 'a', 'a', 'a'], ['t', 'b']]
#print(most_similar_word("a", ["t", "b","f"], build_semantic_descriptors(list), cosine_similarity))

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
# This function takes in a string filename which is the name of a file in the same format as test.txt, and returns the percentage (i.e., float between 0.0 and 100.0) of questions on which most_similar_word() guesses the answer correctly using the semantic descriptors stored in semantic_descriptors, using the similarity function similariy_fn. The format of test.txt is as follows. On each line, we are given a word (all-lowercase), the correct answer, and the choices
    correct = 0
    total = 0
    file = open(filename, "r", encoding = "utf-8-sig")
    file = file.read()
    file = file.lower()
    file = file.split("\n")
    #print(file)
    for line in file:
        total += 1
        line = line.split(" ")
        word = line[0]
        ans = line[1]
        choices = line[2:]
        #print(word, ans, choices)
        guess = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if guess == ans:
            correct += 1
    percent = (correct/total) * 100
    return percent

# semantic1 = build_semantic_descriptors_from_files(["warandpeace.txt"])
# semantic2 = build_semantic_descriptors_from_files(["warandpeace.txt", "swannsway.txt"])

#print(run_similarity_test("test.txt", build_semantic_descriptors_from_files(["warandpeace.txt", "swannsway.txt"]), cosine_similarity))
#print(run_similarity_test("test.txt", build_semantic_descriptors_from_files(["swannsway.txt"]), cosine_similarity))