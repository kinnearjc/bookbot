import string

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents = file_contents
        word_list = file_contents.split()
        return len(word_list)


def get_letter_count(filepath):
    alphabet = set(string.ascii_lowercase)
    letter_dict = {}
    with open(filepath) as f:
        file_contents = f.read().lower()
        for letter in alphabet:
            count = 0
            for char in file_contents:
                if char == letter:
                    count += 1
            letter_dict[letter]  = count
        
    return letter_dict
        
def sorted_dict(my_dict):
    sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict_desc
    