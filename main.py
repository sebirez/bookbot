book = "books/King James Bible.txt"                                         #replace with path to local text file
def main():                                                                 #print report for provided text file
    
    book_text = open_book(book)
    book_words = book_text.split()
    chars_list = list_chars(book_text)
    char_dict = dict_chars(chars_list)
    book_wordcount = word_count(book_words)
    dicted_list = dict_convert(char_dict)
    dicted_list.sort(reverse=True, key=sort_on)

    word_dict = word_frequency(book_words)
    filtered_word_dict = {k: v for k,v in word_dict.items() if len(k) >= 6 }
    max_key = max(filtered_word_dict, key=filtered_word_dict.get)
    min_key = min(filtered_word_dict, key=filtered_word_dict.get)

    print(f"--- Begin report of {book} ---")
    print(book_wordcount, "words found in the document")
    print(f"Most common word: '{max_key}'.")
    print(f"Least common word: '{min_key}'.")

    for dict in dicted_list:
        for key in dict:
            print("The", f"'{key}'", "character was found", f"{dict[key]}", "times")
    print("--- End report ---")
def word_frequency(book_words):                                             #determine frequency of each word 
    word_freq = {}
    for word in book_words:
        if word not in word_freq:
            word_freq[word] = 1
        if word in word_freq: 
            word_freq[word] += 1
    return word_freq
def sort_on(dicted_list):                                                   #define sort method for dicted_list
    return int(list(dicted_list.values())[0])
def dict_convert(char_dict):                                                #convert character dictionary into list of dictionaries
    dict_list = []
    abcs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
    for character in char_dict:
        if character in abcs:
            dict_list.append({f"{character}": f"{char_dict[character]}"})
    return dict_list
def dict_chars(chars_list):                                                 #creates dict of lower-case chars w/ # of occurrences
    char_dict = dict.fromkeys(chars_list, 0)
    for character in char_dict:
        for i in range(len(chars_list)):
            if chars_list[i] == character:
                char_dict[character] += 1
    return char_dict
def list_chars(book_text):                                                  #creates list of lower-case chars
    char_list = []    
    for char in book_text:
        char_list.append(char.lower())
    return char_list
def word_count(book_words):                                                 #returns word count        
    return len(book_words)
def open_book(book):                                                        #opens file
    with open(book) as f:
        return f.read()
main()                                                                      #generate analysis/report
