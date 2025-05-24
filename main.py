from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_count
from sys import argv

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read() 

def generate_report(book_source, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_source}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char in char_count:
        print(f"{char["char"]}: {char["num"]}")


def main():
    if len(argv) != 2:
       print("Usage: python3 main.py <path_to_book>") 
       return sys.exit(1)

    book_source = argv[1]
    book_text = get_book_text(book_source)

    word_count = get_word_count(book_text) 
    char_count = get_char_count(book_text)
    sorted_count = get_sorted_count(char_count)

    generate_report(book_source, word_count, sorted_count)    

main()
