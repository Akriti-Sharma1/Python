import urllib.request
#First, store the number of times that the word w appears in the text in word_counts[w]. For example, if the word “the” appears in the file 5 times, word_counts["the"] should be 5.
#word_counts[w];
def get_word_count():
    words = open("text.txt", encoding="latin-1").read().split()
    #print(words)

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts



#Write a function with the signature top10(L) that takes in a list L of 100 different integers, and returns a list of the 10 largest integers in L.
def top10(L):
    L.sort()
    new = L[-10:]
    return new

#Now, obtain the top 10 most-frequent words from the dictionary freq. To do that, you need to sort the data by the word counts. You cannot sort dictionaries directly, but you can use the following trick:
def obtain_frequent():
    inv_freq = get_word_count()
    L = sorted(inv_freq.values())
    top_10 = top10(L)
    sorted_dict = {}

    for i in top_10:
        for k in inv_freq.keys():
            if inv_freq[k] == i:
                sorted_dict[k] = inv_freq[k]
                break

    print(sorted_dict)

# Problem 2:
def search_address(term):
    url = "https://ca.search.yahoo.com/search?p="+term+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"
    return url
# To search just using the address bar, just enter your entry in here: https://ca.search.yahoo.com/search?p=*CHANGE THIS*&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8
# Define a variable p that equals your search term and then the link will take you there directly

def get_search_results(url1):
    #url = search_address("hello")
    f = urllib.request.urlopen(url1)
    page = f.read().decode("utf-8")
    #page = page.split()
    f.close()
    #print(page)
    #page = list(page)
    #print(page)
    #print(page[3])
    #page.sort()
    for i in range(len(page)):
        if page[i] == "A":
            if page[i+1] == "b":
                if page[i+2] == "o":
                    if page[i+3] == "u":
                        if page[i+4] == "t":
                            j = 0
                            new = []
                            while page[i+j+6] != "s":
                                #print(page[i+j+6])
                                if page[i+j+6] == "," or page[i+j+6] == " ":
                                    j += 1
                                else:
                                    new.append(page[i+j+6])
                                    j += 1
                            break
    string = ""
    for x in new:
        string += x
    string = int(string)
    return string

def choose_variants(variants):
    import urllib
    #print(variants[0])
    #variants[1] = urlib.parse.quote(variants[1])
    url1 = search_address(urllib.parse.quote(variants[0]))
    url2 = search_address(urllib.parse.quote(variants[1]))
    #print(get_search_results(url1),get_search_results(url2))
    if get_search_results(url1) > get_search_results(url2):
        return variants[0]
    else:
        return variants[1]


if __name__ == "__main__":
#     url1 = search_address("hello")
#     get_search_results(url1)
    print(choose_variants(["top ranked school uoft", "top ranked school waterloo"]))
#     # print(word_counts["I"])
#     # L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,96,23,24,25,26,27,28,29,30,31,32,33,34,35,99,37,38,39,40,41,42,43,44,98,46,47,48,49,50,51,52,53,54,55,56,57,58,100,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,22,97,45,36,59]
#     # print(top10(L))
#     obtain_frequent()





