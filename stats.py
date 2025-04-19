import string
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = dict()
    for letter in list(string.ascii_lowercase):
        count = text.lower().count(letter)
        letter_count[letter] = count
    return letter_count

def sort_count_letters(dictionary):
    letter_list = [{"letter":key,"num":value} for key, value in dictionary.items()]
    letter_list.sort(reverse=True, key= lambda x : x["num"])
    return letter_list
