#find_index.py

def find_index(letter, word):
    # Returns all the indices of the "letter" in "word" as a list
    word = word.upper(); letter= letter.upper()
    list_of_index = []
    start = 0
    end = len(word)
    index = 0
    while index != -1:
        index = word.find(letter, start, end)
        start = index + 1 
        list_of_index.append(index)
    del list_of_index[-1]
    return list_of_index