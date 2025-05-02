from stats import *
import sys

def main():
    argument = sys.argv
    
    if (len(argument) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {argument[1]}...")
        
        
        print("----------- Word Count ----------")
        num_words= get_words(argument[1])
        print (f"Found {num_words} total words")


        print("--------- Character Count -------")
        letter_count=get_letter_count(argument[1])
        dict_sorted= sorted_dict(letter_count)
        for key, value in dict_sorted.items():
            print(f"{key}: {value}")

        print("============= END ===============")
main()