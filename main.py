def main():
    book = "books/frankenstein.txt"

    book_text = open_book(book)
    book_words = book_text.split()
    chars_list = list_chars(book_text)
    char_dict = dict_chars(chars_list)
    book_wordcount = word_count(book_words)
    dicted_list = dict_convert(char_dict)
    dicted_list.sort(reverse=True, key=sort_on)

#PRINT REPORT COMPLETE
    print("--- Begin report of books/frankenstein.txt ---")
    print(book_wordcount, "words found in the document")
    print(" ")
    for dict in dicted_list:
        for key in dict:
            print("The", f"'{key}'", "character was found", f"{dict[key]}", "times")
    print("--- End report ---")
#define sort method for dicted_list
def sort_on(dicted_list):
    return int(list(dicted_list.values())[0])
#convert character dictionary into list of dictionaries
def dict_convert(char_dict):
    dict_list = []
    abcs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
    for character in char_dict:
        if character in abcs:
            dict_list.append({f"{character}": f"{char_dict[character]}"})
    return dict_list
#COMPLETE - creates dict of lower-case chars w/ # of occurrences
def dict_chars(chars_list):

    char_dict = dict.fromkeys(chars_list, 0)
    for character in char_dict:
        for i in range(0, len(chars_list)):
            if chars_list[i] == character:
                char_dict[character] += 1

    return char_dict
#COMPLETE - creates list of lower-case chars
def list_chars(book_text):
    char_list = []    
    for char in book_text:
        char_list.append(char.lower())
    return char_list
#COMPLETE - returns word count        
def word_count(book_words):
    return len(book_words)
#COMPLETE - opens file
def open_book(book):   
    with open(book) as f:
        return f.read()
main()